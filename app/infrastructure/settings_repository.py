import sqlite3
from ..domain.models import Settings
from ..domain.repository import SettingsRepository

class SQLiteSettingsRepository(SettingsRepository):

    def __init__(self, db_path):
        self.db_path = db_path
        self._create_table()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        connection = self.get_connection()
        with connection:
            connection.execute(
                '''
                CREATE TABLE IF NOT EXISTS settings (
                    id INTEGER PRIMARY KEY,
                    setpoint_min REAL,
                    setpoint_max REAL,
                    setpoint_offset_summer REAL,
                    setpoint_offset_winter REAL,
                    tolerance REAL,
                    mode_change_delta_temp INTEGER,
                    cascade_time INTEGER,
                    mode INTEGER,
                    mode_switch_timestamp TEXT,
                    mode_switch_lockout_time INTEGER
                )
                '''
            )

    def add_settings(self, settings: Settings):
        connection = self.get_connection()
        with connection:
            connection.execute(
                '''
                INSERT INTO settings (
                    setpoint_min, setpoint_max, setpoint_offset_summer, setpoint_offset_winter,
                    tolerance, mode_change_delta_temp, cascade_time, mode, 
                    mode_switch_timestamp, mode_switch_lockout_time
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    settings.setpoint_min, settings.setpoint_max, settings.setpoint_offset_summer, settings.setpoint_offset_winter,
                    settings.tolerance, settings.mode_change_delta_temp, settings.cascade_time, settings.mode, 
                    settings.mode_switch_timestamp, settings.mode_switch_lockout_time
                )
            )

    def get(self, id: int) -> Settings:
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            '''
            SELECT id, setpoint_min, setpoint_max, setpoint_offset_summer, setpoint_offset_winter,
                   tolerance, mode_change_delta_temp, cascade_time, mode, 
                   mode_switch_timestamp, mode_switch_lockout_time
            FROM settings WHERE id = ?
            ''',
            (id,)
        )
        row = cursor.fetchone()
        if row:
            return Settings(
                id=row[0], setpoint_min=row[1], setpoint_max=row[2], setpoint_offset_summer=row[3],
                setpoint_offset_winter=row[4], tolerance=row[5], mode_change_delta_temp=row[6],
                cascade_time=row[7], mode=row[8], mode_switch_timestamp=row[9], mode_switch_lockout_time=row[10]
            )
        return None

    def list(self) -> list[Settings]:
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            '''
            SELECT id, setpoint_min, setpoint_max, setpoint_offset_summer, setpoint_offset_winter,
                   tolerance, mode_change_delta_temp, cascade_time, mode, 
                   mode_switch_timestamp, mode_switch_lockout_time
            FROM settings
            '''
        )
        rows = cursor.fetchall()
        return [
            Settings(
                id=row[0], setpoint_min=row[1], setpoint_max=row[2], setpoint_offset_summer=row[3],
                setpoint_offset_winter=row[4], tolerance=row[5], mode_change_delta_temp=row[6],
                cascade_time=row[7], mode=row[8], mode_switch_timestamp=row[9], mode_switch_lockout_time=row[10]
            )
            for row in rows
        ]

    def update_settings(self, settings: Settings):
        connection = self.get_connection()
        with connection:
            connection.execute(
                '''
                UPDATE settings
                SET setpoint_min = ?, setpoint_max = ?, setpoint_offset_summer = ?, setpoint_offset_winter = ?,
                    tolerance = ?, mode_change_delta_temp = ?, cascade_time = ?, mode = ?, 
                    mode_switch_timestamp = ?, mode_switch_lockout_time = ?
                WHERE id = ?
                ''',
                (
                    settings.setpoint_min, settings.setpoint_max, settings.setpoint_offset_summer, settings.setpoint_offset_winter,
                    settings.tolerance, settings.mode_change_delta_temp, settings.cascade_time, settings.mode, 
                    settings.mode_switch_timestamp, settings.mode_switch_lockout_time, settings.id
                )
            )
