from typing import Optional, List, Any
from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat


class HabitatManager:

    def __init__(self) -> None:
        habitats: dict[int, Habitat] = {}

    #Section 2.1: Habitat Registration
    def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass
    def remove_habitat(habitat_id: int) -> None:
        pass

    #Setion 2.2: Habitat Retrieval 
    def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]:
        pass
    def get_habitats_by_size(size: int) -> List[Habitat]:
        pass
    def get_habitat_by_id(habitat_id: int) -> Habitat:
        pass
    def get_habitats_by_type(environment_type: str) -> List[Habitat]:
        pass
   

    #Section 2.3: Habitat Details 
    def get_habitat_details(habitat_id: int) -> dict:
        pass
    def get_animals_in_habitat(habitat_id: int) -> List[Animal]:
        pass
    def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
        pass
    def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:
        pass

    #Section 2.4: Assigning Animals to Habitats
    def assign_animals_to_habitat(animals: List[Animal]) -> None:
        pass


    
