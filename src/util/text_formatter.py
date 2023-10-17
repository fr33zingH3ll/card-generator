class TextFormatter:
    def __init__(self, template_length, police_size):
        self.template_length = template_length / police_size

    def format_text(self, input_text):
        words = input_text.split()
        formatted_text = []
        current_line = []

        for word in words:
            if len(" ".join(current_line + [word])) <= self.template_length:
                current_line.append(word)
            else:
                formatted_text.append(" ".join(current_line))
                current_line = [word]

        formatted_text.append(" ".join(current_line))
        return "\n".join(formatted_text)