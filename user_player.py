from game_engine import GameEngine
from console_manager import ConsoleManager
from player import Player # Assuming Player has hp, mp, max_hp, max_mp, etc.
import logging # Optional: for logging actions/errors

logger = logging.getLogger(__name__) # Optional

class UserPlayer(Player):
    """
    Represents a player controlled by the user via the console.
    Handles turn-taking by prompting the user for actions and targets.
    """

    def take_turn(self, game):
        """
        Handles the user's turn by displaying status, prompting for action
        and target (if necessary), and executing the chosen action.

        Args:
            game: The main game object containing the game state, including players.
        """
        ConsoleManager.display_player_status(self) # Show user's HP/MP etc.
        npcs = self._get_npcs(game)
        ConsoleManager.display_targets(npcs) # Show available targets

        if not npcs:
            ConsoleManager.no_targets_alert()
            # Decide what happens here - maybe player can only defend or heal?
            # For now, let's allow heal/defend if no targets
            action = ConsoleManager.prompt_for_user_action(can_attack=False) # Modify prompt if no targets
        else:
            action = ConsoleManager.prompt_for_user_action(can_attack=True)

        target = None # Initialize target

        match action:
            case "a": # Attack
                target = self._select_target(npcs)
                if target:
                    logger.info(f"{self.name} chose to attack {target.name}")
                    GameEngine.attack(self, target)
                else:
                    ConsoleManager.invalid_option_alert("No target selected or available.")
                    self.take_turn(game) # Re-prompt if target selection failed

            case "m": # Magic Attack
                if self.can_cast_magic(): # Check prerequisites (e.g., MP)
                    target = self._select_target(npcs)
                    if target:
                        logger.info(f"{self.name} chose to use magic on {target.name}")
                        GameEngine.magic_attack(self, target)
                    else:
                        ConsoleManager.invalid_option_alert("No target selected or available.")
                        self.take_turn(game) # Re-prompt
                else:
                    ConsoleManager.action_failed_alert("Not enough mana for magic attack!")
                    self.take_turn(game) # Re-prompt

            case "d": # Defend
                logger.info(f"{self.name} chose to defend.")
                self.defend() # Assuming defend is an internal player state change

            case "h": # Heal
                if self.can_heal(): # Check prerequisites (e.g., MP or potions)
                    logger.info(f"{self.name} chose to heal.")
                    GameEngine.heal(self)
                else:
                    ConsoleManager.action_failed_alert("Cannot heal (e.g., no mana or items)!")
                    self.take_turn(game) # Re-prompt

            case "q": # Added a Quit option
                 logger.info(f"{self.name} chose to quit.")
                 GameEngine.quit_game(self) # Signal game engine to handle quitting

            case _:
                ConsoleManager.invalid_option_alert()
                self.take_turn(game) # Re-prompt on invalid action


    def _get_npcs(self, game):
        """Returns a list of all non-user players (NPCs) in the game."""
        # Filter out players that are dead as well
        return [p for p in game.all_players() if not p.is_user() and p.is_alive()]


    def _select_target(self, npcs):
        """
        Allows the user to select a target from the list of available NPCs.

        Args:
            npcs (list): A list of Player objects representing the available NPC targets.

        Returns:
            Player: The selected NPC Player object, or None if selection fails or is cancelled.
        """
        if not npcs:
            # This case should ideally be handled before calling _select_target,
            # but included as a safeguard.
            logger.warning("Attempted to select target when no NPCs are available.")
            ConsoleManager.no_targets_alert()
            return None

        if len(npcs) == 1:
            # Automatically select the only available target
            logger.debug(f"Auto-selecting the only target: {npcs[0].name}")
            return npcs[0]

        # Prompt user to choose from multiple targets
        target_index = ConsoleManager.prompt_for_target_selection(npcs)

        if 0 <= target_index < len(npcs):
            selected_target = npcs[target_index]
            logger.debug(f"User selected target: {selected_target.name}")
            return selected_target
        else:
            # Handle invalid selection (e.g., out of range number, non-numeric input)
            logger.warning(f"Invalid target index received: {target_index}")
            ConsoleManager.invalid_option_alert("Invalid target number.")
            return None # Indicate failed selection


    # --- Prerequisite Checks (Examples - Implement actual logic in Player base class) ---

    def can_cast_magic(self):
        """Placeholder: Check if the player has enough MP for a magic attack."""
        # Example logic (requires Player to have 'mp' and 'magic_cost' attributes/methods)
        # magic_cost = GameEngine.get_magic_attack_cost(self) # Get cost from engine/config
        # return self.mp >= magic_cost
        logger.debug("Placeholder check: can_cast_magic returning True")
        return True # Assume true for now

    def can_heal(self):
        """Placeholder: Check if the player has enough MP or healing items."""
        # Example logic (requires Player to have 'mp', 'heal_cost', 'healing_items' etc.)
        # heal_cost = GameEngine.get_heal_cost(self)
        # has_items = self.healing_items > 0
        # return self.mp >= heal_cost or has_items
        logger.debug("Placeholder check: can_heal returning True")
        return True # Assume true for now

    # --- Player Type Identification ---

    def is_user(self):
        """Identifies this player as user-controlled."""
        return True

    # Removed _first_npc as targeting is now handled by _select_target
    # def _first_npc(self, game):
    #     return [p for p in game.all_players() if not p.is_user()][0]
