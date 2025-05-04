

def calculate_title_prompt_position(title_prompt, start_of_title_height,
                                    title_screen_content, middle_of_window_width):
    middle_of_prompt = int(len(title_prompt) / 2)
    middle_of_window = middle_of_window_width
    title_position = middle_of_window - middle_of_prompt
    title_height = len(title_screen_content)

    title_prompt_height = start_of_title_height + title_height + 2
    return (title_position, title_prompt_height)

def calculate_title_position(title_screen_content, middle_of_window_width, middle_of_window_height):
    return (_calculate_title_position_width(title_screen_content, middle_of_window_width),
            _calculate_title_height(title_screen_content, middle_of_window_height))

def _calculate_title_position_width(title_screen_content, middle_of_window_width):
    title_width = len(title_screen_content[0])
    middle_of_title = int(title_width / 2)
    middle_of_window = middle_of_window_width
    start_of_title = middle_of_window - middle_of_title
    return start_of_title

def _calculate_title_height(title_screen_content, middle_of_window_height):
    title_height = len(title_screen_content)
    middle_of_title_height = int(title_height / 2)
    start_of_title_height = middle_of_window_height - middle_of_title_height
    return start_of_title_height
