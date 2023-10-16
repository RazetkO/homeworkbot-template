from dataclasses import dataclass


@dataclass
class DbCreatorSetting:
    remote_configuration: bool
    default_admin: int | None = None
    disciplines_path: str = ''
    execel_data_path: str = ''
