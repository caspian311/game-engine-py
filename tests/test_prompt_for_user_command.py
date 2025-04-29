from game.prompt_for_user_command import PromptForUserCommand
from game.data import DATA

def test_prompt_for_user_changes_state_to_prompt_for_user():
    DATA.state.prompt_for_user = False

    PromptForUserCommand().execute([])

    assert DATA.state.prompt_for_user
