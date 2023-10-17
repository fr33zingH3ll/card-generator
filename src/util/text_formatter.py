class TextFormatter:
    def __init__(self, template_length, police_size):
        self.template_length = template_length/police_size

    def format_text(self, input_text):
        words = input_text.split()
        formatted_text = ""
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= self.template_length:
                current_line += word + " "
            else:
                formatted_text += current_line + "\n"
                current_line = word + " "

        formatted_text += current_line  # Ajouter la dernière ligne
        return formatted_text