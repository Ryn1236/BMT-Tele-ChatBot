from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
)
from pathlib import Path


TELEGRAM_TOKEN = "Telegram Bot Token"

VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("Start", callback_data="start")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome, Parents! 👋\n\n"
        "Sending your son for Basic Military Training (BMT) can be "
        "a new and unfamiliar experience for both you and your family. "
        "OneBMT Chatbot is here to help you better understand what your son "
        "will experience during his time in BMT.\n\n"
        "📚 Learn more about the different activities and training "
        "your son will go through, from IPPT and route marches to "
        "field camp, weapon training and National Education.\n\n"
        "💡 Each section provides simple explanations to help you "
        "understand what the activity is, what your son will be doing "
        "and why it is part of BMT.\n\n"
        "❤️ We hope OneBMT Chatbot gives you greater peace of mind and helps "
        "you feel more informed throughout your son's BMT journey.\n\n"
        "Tap the button below to get started! 👇",
        reply_markup=reply_markup
    )


async def delete_current_message(query):
    try:
        await query.message.delete()
    except Exception:
        pass


async def handle_callback_query(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "start":

        response_text = "WELCOME TO 12C4I OneBMT."
        image_path = IMAGE_DIR / "12C4I Logo.png"

        if image_path.exists():

            with open(image_path, "rb") as photo:
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=photo,
                    caption=response_text
                )

        else:

            await query.message.reply_text(
                f"{response_text}\n\n"
                f"Image not found:\n{image_path}"
            )

        await menu_keyboard(update, context)


    elif data == "activity":

        await delete_current_message(query)
        await highkey_keyboard(update, context)


    elif data == "weapon":

        await delete_current_message(query)

        response_text = (
            "Recruits learn how to safely handle, carry, present "
            "and care for their service weapon. They are taught "
            "proper safety procedures, discipline and how to follow "
            "commands when handling the weapon. This forms the "
            "foundation for later shooting and field training, where "
            "recruits must be able to handle their weapon safely "
            "and confidently."
        )

        await send_activity(
            update,
            context,
            response_text,
            "weapon presentation.jpeg"
        )


    elif data == "ippt":

        await delete_current_message(query)

        response_text = (
            "IPPT (Individual Physical Proficiency Test) training "
            "helps recruits improve their running ability, strength, "
            "stamina and overall fitness. Training is progressive "
            "and prepares them for both the IPPT and the physical "
            "demands of BMT. Recruits may find the training tiring "
            "at first, especially if they are not used to regular "
            "exercise, but their fitness is developed progressively "
            "throughout BMT."
        )

        await send_activity(
            update,
            context,
            response_text,
            "ippt training.jpeg"
        )


    elif data == "strength":

        await delete_current_message(query)

        response_text = (
            "Strength training develops the muscular strength and "
            "endurance needed for military activities. Recruits "
            "perform physical exercises that help prepare them for "
            "tasks such as carrying equipment, overcoming obstacles "
            "and completing demanding activities. It also helps "
            "recruits build physical resilience and become more "
            "capable of handling the demands of military training."
        )

        await send_activity(
            update,
            context,
            response_text,
            "strength training.jpeg"
        )


    elif data == "soc":

        await delete_current_message(query)

        response_text = (
            "The Standard Obstacle Course (SOC) consists of a "
            "series of physical obstacles that recruits must learn "
            "to overcome. It tests strength, agility, balance, "
            "coordination and endurance. Besides physical fitness, "
            "SOC helps develop confidence, determination and "
            "resilience as recruits learn to overcome challenging "
            "obstacles."
        )

        await send_activity(
            update,
            context,
            response_text,
            "soc.jpeg"
        )


    elif data == "bic":

        await delete_current_message(query)

        response_text = (
            "The Battle Inoculation Course (BIC) exposes recruits "
            "to a controlled and realistic military training "
            "environment. Recruits apply skills they have learnt "
            "while dealing with physical and environmental "
            "challenges. The activity helps develop resilience, "
            "confidence, teamwork and the ability to remain focused "
            "under pressure."
        )

        await send_activity(
            update,
            context,
            response_text,
            "bic.jpeg"
        )


    elif data == "swim":

        await delete_current_message(query)

        response_text = (
            "Swimming training develops recruits' water confidence, "
            "swimming ability and physical endurance. Recruits with "
            "different swimming abilities are progressively trained "
            "to become more comfortable and capable in the water. "
            "The training also provides an important safety skill "
            "while contributing to their overall physical fitness."
        )

        await send_activity(
            update,
            context,
            response_text,
            "swimming.jpeg"
        )


    elif data == "march":

        await delete_current_message(query)

        response_text = (
            "Route marches involve recruits marching together over "
            "set distances while carrying their required equipment. "
            "The distance and physical demands increase as training "
            "progresses. These marches develop endurance, discipline, "
            "teamwork and mental resilience while teaching recruits "
            "how to manage fatigue and continue working together "
            "as a group."
        )

        await send_activity(
            update,
            context,
            response_text,
            "route march.jpeg"
        )


    elif data == "BTP":

        await delete_current_message(query)

        response_text = (
            "The Basic Trainfire Package (BTP) introduces recruits "
            "to basic military marksmanship and shooting. It builds "
            "upon the weapon-handling skills they have learnt earlier "
            "in BMT. Recruits learn the fundamentals of shooting "
            "while following strict safety procedures and instructions. "
            "The training develops discipline, focus and confidence "
            "when handling their weapon."
        )

        await send_activity(
            update,
            context,
            response_text,
            "BTP.jpeg"
        )


    elif data == "IFC":

        await delete_current_message(query)

        response_text = (
            "Individual Field Craft (IFC) teaches recruits the basic "
            "skills needed to operate in an outdoor military "
            "environment. They learn how to manage themselves and "
            "their equipment while adapting to field conditions. "
            "Recruits may experience heat, humidity, rain, mud and "
            "other outdoor conditions, helping them develop resilience, "
            "independence and adaptability."
        )

        await send_activity(
            update,
            context,
            response_text,
            "IFC.jpeg"
        )


    # elif data == "outfield":

    #     await delete_current_message(query)

    #     response_text = (
    #         "Field Camp gives recruits the opportunity to apply "
    #         "their soldiering and fieldcraft skills in an outdoor "
    #         "environment. They spend an extended period away from "
    #         "normal camp facilities while managing their equipment "
    #         "and working as a team. The experience develops resilience, "
    #         "teamwork, adaptability and independence. Parents should "
    #         "not be surprised if their son returns tired, dirty or "
    #         "uncomfortable after outfield training."
    #     )

    #     await send_activity(
    #         update,
    #         context,
    #         response_text,
    #         "outfield.jpeg"
    #     )


    elif data == "UO":

        await delete_current_message(query)

        response_text = (
            "Urban Operations introduces recruits to operating in "
            "built-up environments such as areas with buildings and "
            "roads. Training focuses on teamwork, communication, "
            "movement and awareness of their surroundings. It teaches "
            "recruits how to work effectively as a team while adapting "
            "to the challenges of an urban environment."
        )

        await send_activity(
            update,
            context,
            response_text,
            "UO.jpeg"
        )


    elif data == "grenade":

        await delete_current_message(query)

        response_text = (
            "Grenade training teaches recruits the required safety "
            "procedures and techniques for handling and throwing "
            "grenades in a controlled training environment. Safety "
            "and discipline are heavily emphasised throughout the "
            "activity. Recruits must follow instructions carefully "
            "and remain focused while handling the grenade."
        )

        await send_activity(
            update,
            context,
            response_text,
            "grenade.jpeg"
        )


    elif data == "NE":

        await delete_current_message(query)

        response_text = (
            "National Education Tour helps recruits understand "
            "Singapore's history, security environment and the "
            "importance of national defence. It gives them greater "
            "context about why National Service exists and their role "
            "in defending Singapore. It also helps recruits understand "
            "that BMT is not only about physical and military skills, "
            "but also about developing a sense of responsibility and "
            "commitment to Singapore."
        )

        await send_activity(
            update,
            context,
            response_text,
            "nationaledu.jpeg"
        )


    elif data == "back":

        await delete_current_message(query)
        await highkey_keyboard(update, context)


    elif data == "menu":

        await delete_current_message(query)
        await menu_keyboard(update, context)


    elif data == "call":

        await delete_current_message(query)

        response_text = (
            "📧 <b>CO 12 C4I</b>\n\n"
            'Email: <a href="mailto:George_Liu_Jun@defence.gov.sg">George_Liu_Jun@defence.gov.sg</a>'
        )

        keyboard = [
            [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="menu")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response_text,
            reply_markup=reply_markup,
            parse_mode="HTML"
        )


    elif data == "faq":

        await delete_current_message(query)

        keyboard = [
            [
                InlineKeyboardButton(
                    "📱 When can I contact my son?",
                    callback_data="faq1"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏥 What if my son gets sick or injured?",
                    callback_data="faq2"
                )
            ],
            [
                InlineKeyboardButton(
                    "⏰ What is a typical day like in BMT?",
                    callback_data="faq3"
                )
            ],
            [
                InlineKeyboardButton(
                    "💪 How difficult is BMT?",
                    callback_data="faq4"
                )
            ],
            [
                InlineKeyboardButton(
                    "❤️ How can I support my son?",
                    callback_data="faq5"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 Main Menu",
                    callback_data="menu"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                "❓ Frequently Asked Questions\n\n"
                "Select a question below to view the answer:"
            ),
            reply_markup=reply_markup
        )


    elif data == "faq1":

        await delete_current_message(query)

        response_text = (
            "📱 When can I contact my son, and how often can he use "
            "his phone?\n\n"

            "During BMT, recruits have limited access to their phones, "
            "especially during training hours. They will generally "
            "have opportunities to use their phones during designated "
            "periods, such as after training or during book-out.\n\n"

            "The exact timings can differ depending on the company, "
            "training schedule and circumstances. If your son does "
            "not reply immediately, it usually means he is busy with "
            "training rather than anything being wrong."
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 Back to FAQ",
                    callback_data="faq"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response_text,
            reply_markup=reply_markup
        )


    elif data == "faq2":

        await delete_current_message(query)

        response_text = (
            "🏥 What happens if my son gets sick or injured?\n\n"

            "The SAF has medical facilities and trained medical "
            "personnel to attend to recruits who become sick or "
            "injured.\n\n"

            "Your son should inform his commanders or the medic if "
            "he is feeling unwell or injured. Depending on the "
            "severity, he may receive treatment, be given medical "
            "rest or be referred for further medical attention.\n\n"

            "Parents will generally be informed when the situation "
            "requires it."
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 Back to FAQ",
                    callback_data="faq"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response_text,
            reply_markup=reply_markup
        )


    elif data == "faq3":

        await delete_current_message(query)

        response_text = (
            "⏰ What is a typical day like in BMT?\n\n"

            "A typical day is structured and can be physically "
            "demanding.\n\n"

            "Recruits will usually wake up early, attend morning "
            "activities, have meals, and take part in training such "
            "as physical training, drills, weapon training, lectures "
            "and other soldiering activities.\n\n"

            "There will also be time for meals, administrative "
            "matters and personal hygiene. The schedule varies "
            "depending on the day's training."
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 Back to FAQ",
                    callback_data="faq"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response_text,
            reply_markup=reply_markup
        )


    elif data == "faq4":

        await delete_current_message(query)

        response_text = (
            "💪 How difficult is BMT?\n\n"

            "BMT can be challenging both physically and mentally, "
            "especially during the first few weeks as recruits adjust "
            "to military life.\n\n"

            "However, training is progressive and recruits are not "
            "expected to be perfect from the start. They will gradually "
            "build up their physical fitness, military skills and "
            "confidence throughout training."
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 Back to FAQ",
                    callback_data="faq"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response_text,
            reply_markup=reply_markup
        )


    elif data == "faq5":

        await delete_current_message(query)

        response_text = (
            "❤️ How can I support my son during BMT?\n\n"

            "The best way parents can help is by being supportive "
            "and encouraging.\n\n"

            "Listen to your son when he wants to talk, reassure him "
            "when he is having a difficult day, and avoid putting "
            "additional pressure on him.\n\n"

            "Even a simple message telling him to take care and keep "
            "going can mean a lot. Let him know that you are proud "
            "of his effort and that it is okay to take some time to "
            "adjust to military life."
        )

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 Back to FAQ",
                    callback_data="faq"
                )
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response_text,
            reply_markup=reply_markup
        )

    else:

        await delete_current_message(query)

        response_text = "Sorry, I didn't understand that."

        keyboard = [
            [InlineKeyboardButton("🔙 Back to Activities", callback_data="activity")],
            [InlineKeyboardButton("🏠 Main Menu", callback_data="menu")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response_text,
            reply_markup=reply_markup
        )


async def send_activity(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    response_text: str,
    image_name: str
):

    image_path = IMAGE_DIR / image_name

    keyboard = [
        [InlineKeyboardButton("🔙 Back to Activities", callback_data="back")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if image_path.exists():

        with open(image_path, "rb") as photo:

            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=photo,
                caption=response_text,
                reply_markup=reply_markup
            )

    else:

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                f"{response_text}\n\n"
                f"Image not found:\n{image_path}"
            ),
            reply_markup=reply_markup
        )


async def menu_keyboard(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [

        [
            InlineKeyboardButton(
                "Activities",
                callback_data="activity"
            )
        ],

        [
            InlineKeyboardButton(
                "Contact Us",
                callback_data="call"
            )
        ],

        [
            InlineKeyboardButton(
                "FAQ",
                callback_data="faq"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(

        chat_id=update.effective_chat.id,

        text=(
            "Basic Military Training (BMT) is a rite of passage "
            "every full-time National Serviceman (NSF). "

            "Click below to find out more!"
        ),

        reply_markup=reply_markup
    )


async def highkey_keyboard(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    keyboard = [

        [
            InlineKeyboardButton(
                "Weapon Handling and Presentation 🔫",
                callback_data="weapon"
            )
        ],

        [
            InlineKeyboardButton(
                "IPPT Training 🏃",
                callback_data="ippt"
            )
        ],

        [
            InlineKeyboardButton(
                "Strength Training 💪",
                callback_data="strength"
            )
        ],

        [
            InlineKeyboardButton(
                "Standard Obstacle Course (SOC) 🧗",
                callback_data="soc"
            )
        ],

        [
            InlineKeyboardButton(
                "Battle Inoculation Course (BIC) 🪖",
                callback_data="bic"
            )
        ],

        [
            InlineKeyboardButton(
                "Swimming 🏊",
                callback_data="swim"
            )
        ],

        [
            InlineKeyboardButton(
                "Route Marches 🥾",
                callback_data="march"
            )
        ],

        [
            InlineKeyboardButton(
                "Basic Trainfire Package (BTP) 🎯",
                callback_data="BTP"
            )
        ],

        [
            InlineKeyboardButton(
                "Individual Field Craft (IFC) 🌳",
                callback_data="IFC"
            )
        ],

        # [
        #     InlineKeyboardButton(
        #         "Field Camp (Outfield) ⛺",
        #         callback_data="outfield"
        #     )
        # ],

        [
            InlineKeyboardButton(
                "Urban Operations 🏙️",
                callback_data="UO"
            )
        ],

        [
            InlineKeyboardButton(
                "Grenade Throwing 💣",
                callback_data="grenade"
            )
        ],

        [
            InlineKeyboardButton(
                "National Education Tour 🇸🇬",
                callback_data="NE"
            )
        ],

        [
            InlineKeyboardButton(
                "Main Menu 🏠",
                callback_data="menu"
            )
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(

        chat_id=update.effective_chat.id,

        text=(
            "Explore the activities below to learn more about your son's BMT journey. 👇"
        ),

        reply_markup=reply_markup
    )


def main():

    application = (
        Application.builder()
        .token(TELEGRAM_TOKEN)
        .build()
    )

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CallbackQueryHandler(handle_callback_query)
    )

    print(
        f"BMT ChatBot (Version {VERSION}) is running..."
    )

    application.run_polling()


if __name__ == "__main__":
    main()
