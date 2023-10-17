import argparse
import json
import pathlib
from PIL import Image, ImageFont, ImageDraw
from util.text_formatter import TextFormatter

from card_content.flashcard_categs import FlashCardCategs
from mechanics.card import Card


OPTIONS = {}



def render_cards(card_json_path, output_path):
    new_card_render_path = pathlib.Path(output_path, "renders")
    new_card_json_path = pathlib.Path(card_json_path, "cards")

    fichiers_json = [fichier for fichier in new_card_json_path.glob("*.json")]

    for fichier in fichiers_json:

        with open(fichier, encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                card = card_from_json(item)
                card_image = render_card(card)
                image_name = f"{card.index:03d}_{card.snake_case_name}.png"
                card_image.save(new_card_render_path / f"{image_name}")


def render_card(card: Card):
    print(f"Rendering {card.name}")
    template = Image.open(f"resources/templates/{card.image_file}.png")
    W, H = template.size
    font_size_question = 36
    font_size_name = 20
    font_size_response = 30
    init_options({
        "w": W,
        "h": H,
        "font_color": "white",
        "font_size_name": font_size_name,
        "font_name": ImageFont.truetype("resources/font/Cabin-Bold.ttf", font_size_name),
        "font_size_question": font_size_question,
        "font_question": ImageFont.truetype("resources/font/Cabin-Bold.ttf", font_size_question),
        "font_size_response": font_size_response,
        "font_response": ImageFont.truetype("resources/font/Cabin-Bold.ttf", font_size_response)  
    })
    # Créer un objet ImageDraw pour dessiner sur l'image
    draw_question = ImageDraw.Draw(template)

    text_formater = TextFormatter(OPTIONS['w'], OPTIONS['font_size_response'])
    
    render_name(card, draw_question)
    render_question(card, draw_question)
    
    template_response = template.rotate(180)
    draw_response = ImageDraw.Draw(template_response)

    render_response(card, draw_response, [text_formater])

    template = template_response.rotate(180)

    return template

def render_name(card, image):
    global OPTIONS
    name_card = card.name
    _, _, w, h = image.textbbox((0, 0), name_card, font=OPTIONS['font_name'])
    position_question = ((OPTIONS['w'] - w) / 30, ((OPTIONS['h'] - h ) / 30)*29)
    image.text(position_question, name_card, font=OPTIONS['font_name'], fill=OPTIONS['font_color'])

def render_question(card, image):
    global OPTIONS
    # Texte de la question
    question = f"{card.index}. {card.question}"
    _, _, w, h = image.textbbox((0, 0), question, font=OPTIONS['font_question'])
    position_question = ((OPTIONS['w'] - w) / 2, (OPTIONS['h'] - h) / 4)
    image.text(position_question, question, font=OPTIONS['font_question'], fill=OPTIONS['font_color'])

def render_response(card, image, list):
    global OPTIONS
    if isinstance(list[0], TextFormatter) :
        response = list[0].format_text(card.response)
    _, _, w, h = image.textbbox((0, 0), response, font=OPTIONS['font_response'])    
    position_response = ((OPTIONS['w'] - w) / 2, (OPTIONS['h'] - h) / 4)
    image.text(position_response, response, font=OPTIONS['font_response'], fill=OPTIONS['font_color'])



def card_from_json(data: dict) -> Card:
    card = Card(
        index=data["index"],
        name=data["name"],
        question=data['question'],
        response=data['response'],
        categ=FlashCardCategs.get_categ_by_name(data["categ"]),
        image_file=data['image_file']
    )
    return card

def init_options(list_option):
    global OPTIONS
    OPTIONS = list_option

def main():
    output_argparser = argparse.ArgumentParser()
    output_argparser.add_argument(
        "--collection",
        help="File path to the collection to render",
        default="output/",
    )
    card_json_argparser =  argparse.ArgumentParser()
    card_json_argparser.add_argument(
        "--collection",
        help="File path to the collection to render",
        default="resources/",
    )
    output_path = output_argparser.parse_args().collection
    card_json_path = card_json_argparser.parse_args().collection
    render_cards(card_json_path, output_path)


if __name__ == "__main__":
    main()
