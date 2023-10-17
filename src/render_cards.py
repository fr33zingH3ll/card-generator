import argparse
import json
import pathlib
from PIL import Image, ImageFont, ImageDraw
from util.text_formatter import TextFormatter

from pokemon_content.flashcard_categs import FlashCardCategs
from mechanics.card import Card


MONSTER_IMAGE_SCALE = 0.255
MONSTER_IMAGE_SCALE_SQ = 0.355
IDEAL_CARD_WIDTH = 390

ABILITY_WIDTH = 370
ABILITY_HEIGHT = 72
ABILITY_COST_WIDTH = 76
ABILITY_COST_GAP = 12
ELEMENT_SIZE = 30
ABILITY_GAP = 4
POWER_WIDTH = 64

STATUS_Y_POSITION = 568
STATUS_X_GAP = 82
STATUS_SIZE = 20


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
    options = {
        font_size_question: 36,
        font_question: ImageFont.truetype("resources/font/Cabin-Bold.ttf", font_size_question),        
    }
    # Charger une police TrueType (TTF) avec la taille spécifiée
    font_size_question = 36  # Taille de police (modifiable selon vos besoins)
    font_question = ImageFont.truetype("resources/font/Cabin-Bold.ttf", font_size_question)
    font_size_response = 30  # Taille de police (modifiable selon vos besoins)
    font_response = ImageFont.truetype("resources/font/Cabin-Bold.ttf", font_size_response)
    fontColor="white"
    
    # Charger le template PNG
    template_question = Image.open(f"resources/templates/{card.image_file}.png")

    # Créer un objet ImageDraw pour dessiner sur l'image
    draw_question = ImageDraw.Draw(template_question)

    # Obtenir les dimensions de l'image
    W, H = template_question.size

    text_formater = TextFormatter(W, font_size_response)

    render_name(card, draw_question, )
    # Texte de la question
    question = card.question
    _, _, w, h = draw_question.textbbox((0, 0), question, font=font_question)
    position_question = ((W - w) / 2, (H - h) / 4)
    draw_question.text(position_question, question, font=font_question, fill=fontColor)

    template_response = template_question.rotate(180)

    # Créer un objet ImageDraw pour dessiner sur l'image
    draw_response = ImageDraw.Draw(template_response)
    
    # Texte de la réponse
    response = text_formater.format_text(card.response)
    _, _, w, h = draw_response.textbbox((0, 0), response, font=font_response)    
    position_response = ((W - w) / 2, (H - h) / 4)
    draw_response.text(position_response, response, font=font_response, fill=fontColor)

    template = template_response.rotate(180)

    return template

def render_name(card, image, option_dict):
    name_card = f"{card.index}.{card.name}"
    _, _, w, h = image.textbbox((0, 0), name_card, font=option_dict['font_question'])
    position_question = ((W - w) / 2, (H - h) / 6)
    image.text(position_question, name_card, font=option_dict['font_question'], fill=option_dict['fontColor'])


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
