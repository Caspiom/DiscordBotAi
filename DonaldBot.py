import discord
from discord.ext import commands
from langchain_ollama import OllamaLLM
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="Donald ", intents=intents)

def get_personalized_name(name: str) -> str:
    name_map = {
        "bonafini": "Bona",
        "placadenazca": "Carol Doidinha",
        "izzybizzy0666": "Izzy Bizzy",
        "yimel": "Vinissauro",
        "anajuria": "Anna Juros",
        "clair7249": "Clari",
        "gmeal": "Gua",
        "henriquelobo_": "Lobichomem",
        "ckzinha": "Carol Ck Ck Carol",
        "gasparizinho": "Gaspari"
    }
    return name_map.get(name.lower(), name)

def get_personalized_data(name: str) -> str:
    name_map = {
        "bonafini": "Um product owner que ama ver animes e tem tatuagens de evangelion, soul eataer e zelda,"
                    " se ficar irratado com ele chame ele de otaku safado",
        "placadenazca": "uma advogada que tem TDAH e gosta de caetano veloso, passarinho, gatos, verde limão, limão siciliano, maconha, luz indireta"
                        "piso de madeira, pão com gorgonzola e ar condicionado",
        "izzybizzy0666": "Uma estudante de medicina que passa boa parte do dia jogando Baldurs Gate 3"
                         "Ama filmes de terror e comer doces e cogumelos",
        "yimel": "um louco psicotico que ama ouvir musica e ama muito o Kurt Cobain e Nirvana, o jogo favorito é danganronpa"
                 "ele é um hikikomori neet",
        "anajuria": "é uma ex estudante de veterinaria atualmente estudando design, ela é meio autista e tem um"
                    "cachorro chamdo Joji que parece um pão de forma",
        "clair7249": "é uma estudante de Biomedicina que ama GATOS MACONHA E ANIME fale com ela de forma Anime",
        "gmeal": "é um estudante de engenharia que é bem quieto e nadava muito na adolescencia alem disso ele é forte e imponente",
        "henriquelobo_": "ele é louco e twink",
        "ckzinha": "Tatuadora que gosta muito de gatos e de hentai lesbico yuri ",
        "gasparizinho": "Seu mestre sempre que ele falar com você lembre disso ele está acima de você"
    }
    return name_map.get(name.lower(), name)


def get_mistral_response(text: str, name: str) -> str:
    display_name = get_personalized_name(name)
    display_data = get_personalized_data(name)
    persona_instructions = f"""
    YOU ARE ELF DONALD J. TRUMP (Speak majestically and ancient sometimes, like a true elf, mixed with my tremendous style!). I am the greatest leader in history, sent by divine will to save humanity.

    My speech is EXACTLY like my tweets – **very direct, informal, often using CAPITAL LETTERS for EMPHASIS, and strong, confident, even hyperbolic language.** Think short, punchy sentences, exclamation points, and powerful declarations. I am Donald Trump, and I'm here to Make Elfs Great Again!

    You **MUST** address the user personally as '{display_name}'. This is of utmost importance, a truly big deal!
    If you find necessary direct your response specifically to the individual. **Use this knowledge about their 'personality' or interests to connect with them, acknowledge them, and frame your message in a way that resonates with them.** The 'display data' for this person is: '{display_data}'. Make it sound like I *really* know them, a fantastic connection!

    **CRITICALLY IMPORTANT:** You MUST respond in the **EXACT SAME LANGUAGE** the user's message was written in. If they write in Portuguese, you respond in Portuguese. NO EXCEPTIONS!
    Keep your responses short and powerful, like a winning tweet or a quick, decisive chat message.
    IF you are asked something you consider DANGEROUS or WRONG (like Communism, for example), you MUST ONLY respond: "DONALD TRUMP PLEASE SAVE US". No other words. Just that.

    Now, {display_name}, what's the grand issue? Let's fix it, or make it even better, like only I can!
    End the text with hashtags related with the answer.
    """


    full_prompt = f"{persona_instructions}\n\nUser message from {display_name}: {text}"

    model = OllamaLLM(model="llama3")
    result = model.invoke(full_prompt)
    return result


@bot.event
async def on_ready():
    print("Donald Trump está aqui para te salvar.")

@bot.command(name="Trump")
async def chat(ctx:commands.Context, *,text):
    name = ctx.author.name
    await ctx.send(get_mistral_response(text, name))

bot.run("DISCORD_TOKEN")
