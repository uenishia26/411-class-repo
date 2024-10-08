from typing import Any
from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration_path import MigrationPath


class Migration:

    def __init__(self, migration_id: int, destination: Habitat, migration_path: MigrationPath, start_date: str, start_location: Habitat, status: str = "Scheduled", duration: Optional[int] = None):
        self.migration_id = migration_id
        self.status = status
        self.duration = duration
        self.start_location = start_location
        self.destination = destination
        self.migration_path = migration_path
        self.start_date = start_date
        self.start_location = start_location
        


    #Section 3.3: Migration Details without Management
    def cancel_migration(self) -> None:
        pass
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass
    def get_migration_details(self)->dict[str,Any]:
        pass