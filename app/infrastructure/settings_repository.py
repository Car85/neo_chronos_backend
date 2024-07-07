import sqlite3
from ..domain.models import Settings
from ..domain.repository import UserSettingsRepository

class SQLiteSettingsRepository(UserSettingsRepository):

    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def get_settings(self) -> Settings:
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM settings LIMIT 1')
        row = cursor.fetchone()
        if row:
            return Settings(
                id=row[0],
                setpoint_min=row[1],
                setpoint_max=row[2],
                setpoint_offset_summer=row[3],
                setpoint_offset_winter=row[4],
                tolerance=row[5],
                mode_change_delta_temp=row[6],
                cascade_time=row[7],
                mode=row[8],
                mode_switch_timestamp=row[9],
                mode_switch_lockout_time=row[10]
            )
        return None

    def update_settings(self, settings: Settings) -> None:
        connection = self.get_connection()
        with connection:
            connection.execute('''
                UPDATE settings
                SET setpoint_min = ?,
                    setpoint_max = ?,
                    setpoint_offset_summer = ?,
                    setpoint_offset_winter = ?,
                    tolerance = ?,
                    mode_change_delta_temp = ?,
                    cascade_time = ?,
                    mode = ?,
                    mode_switch_timestamp = ?,
                    mode_switch_lockout_time = ?
                WHERE id = ?
            ''', (
                settings.setpoint_min,
                settings.setpoint_max,
                settings.setpoint_offset_summer,
                settings.setpoint_offset_winter,
                settings.tolerance,
                settings.mode_change_delta_temp,
                settings.cascade_time,
                settings.mode,
                settings.mode_switch_timestamp,
                settings.mode_switch_lockout_time,
                settings.id
            ))
