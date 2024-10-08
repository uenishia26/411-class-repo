from typing import Any
from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration_path import MigrationPath


class MigrationPath:

    def __init__(self, path_id: int, current_date: str, current_location: str):
        self.path_id = path_id
        self.current_date = current_date
        self.current_location = current_location

    def create_migration_path(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def get_migration_path_details(self) -> dict:
        pass

    def remove_migration_path(self) -> None:
        pass

    def update_migration_path_details(self, **kwargs) -> None:
        pass