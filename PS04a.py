# Программа, с помощью которой можно искать информацию на Википедии с помощью консоли.
# - Спрашивать у пользователя первоначальный запрос.
# - Переходить по первоначальному запросу в Википедии.
# - Предлагать пользователю три варианта действий:
# 1. листать параграфы текущей статьи;
# 2. перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# 3. выйти из программы.
# изначальный язык английский, затем определение языка ввода пользователя, 
# на котором будет запрос и последующие ответы на языке пользователя

import wikipedia
from langdetect import detect


def choose_action():
    print("\nActions:")
    print("1 - Read article paragraphs")
    print("2 - Follow a linked article")
    print("3 - Exit")
    return input("Enter action number: ")


def show_paragraphs(paragraphs):
    index = 0
    while index < len(paragraphs):
        print("\n---")
        print(paragraphs[index])
        cont = input("\nNext paragraph? (y/n): ").lower()
        if cont == 'y':
            index += 1
        else:
            break
    if index >= len(paragraphs):
        print("\nEnd of article.")


def follow_link(links):
    if not links:
        print("No linked articles found.")
        return None

    index = 0
    while index < len(links):
        current_batch = links[index:index + 10]
        for i, link in enumerate(current_batch, start=index + 1):
            print(f"{i}. {link}")

        choice = input("\nEnter article number to open (0 to cancel, n for next batch): ")
        if choice == 'n':
            index += 10
            if index >= len(links):
                print("No more articles.")
                index = 0  # Если кончились статьи — начать сначала
        elif choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print("Canceled.")
                return None
            if 1 <= choice <= len(links):
                return links[choice - 1]
            else:
                print("Invalid number.")
        else:
            print("Invalid input.")
    return None


def handle_article(page):
    while True:
        action = choose_action()
        if action == '1':
            paragraphs = page.content.split('\n\n')
            show_paragraphs(paragraphs)
        elif action == '2':
            link = follow_link(page.links)
            if link:
                try:
                    page = wikipedia.page(link)
                except wikipedia.exceptions.DisambiguationError as e:
                    print("Multiple options found:")
                    for i, option in enumerate(e.options, start=1):
                        print(f"{i}. {option}")
                    choice = input("Enter number: ")
                    if choice.isdigit() and 1 <= int(choice) <= len(e.options):
                        page = wikipedia.page(e.options[int(choice) - 1])
                    else:
                        print("Invalid choice. Staying on the current page.")
                except wikipedia.exceptions.PageError:
                    print("Page not found.")
            else:
                continue
        elif action == '3':
            print("Bye!")
            break
        else:
            print("Invalid action.")


def search_wikipedia():
    query = input("Enter your topic: ").strip()
    if not query:
        print("Empty input.")
        return

    # Определяем язык
    try:
        lang = detect(query)
    except:
        lang = 'en'

    wikipedia.set_lang(lang if lang in wikipedia.languages() else 'en')
    print(f"Language detected: {lang}")

    try:
        page = wikipedia.page(query)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Multiple options found:")
        for i, option in enumerate(e.options, start=1):
            print(f"{i}. {option}")
        choice = input("Enter number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(e.options):
            page = wikipedia.page(e.options[int(choice) - 1])
        else:
            print("Invalid choice.")
            return
    except wikipedia.exceptions.PageError:
        print("Page not found.")
        return

    print(f"\n=== {page.title} ===")
    handle_article(page)


search_wikipedia()
