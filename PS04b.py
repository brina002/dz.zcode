from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get("https://en.wikipedia.org")

assert "Wikipedia" in browser.title

search_box = browser.find_element(By.NAME, "search")
user_query = input("Enter what you want to search on Wikipedia: ")
search_box.send_keys(user_query)
search_box.send_keys(Keys.RETURN)
time.sleep(5)


def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    if not paragraphs:
        print("No paragraphs found on the page.")
    else:
        for idx, p in enumerate(paragraphs):
            # Scroll to the paragraph
            browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", p)
            # Highlight the paragraph
            browser.execute_script("arguments[0].style.backgroundColor = 'yellow';", p)
            print(f"\nParagraph {idx + 1}:\n{p.text}")
            next_action = input("\nPress Enter to continue to the next paragraph or type 'q' to return to the menu: ")

            # Remove highlight if user continues
            browser.execute_script("arguments[0].style.backgroundColor = '';", p)

            if next_action.lower() == 'q':
                break


def choose_link():
    # Выполняем JavaScript-код прямо в браузере
    result = browser.execute_script("""
        const anchors = Array.from(document.querySelectorAll('a'));
        return anchors
            .filter(a => a.href.includes('/wiki/') && a.innerText.trim().length > 0)
            .map(a => {
                let cleanText = a.innerText.trim();
                // Убираем начальные цифры с точками (например "4.5.3 ")
                cleanText = cleanText.replace(/^\\d+(\\.\\d+)*\\s*/, '');
                return { text: cleanText, href: a.href };
            })
            .filter(a => a.text.length > 1) // Чтобы не брать пустые строки
            .slice(0, 20);
    """)

    if not result:
        print("No suitable links found on the page.")
        return

    print("\nAvailable topics to visit:")
    for i, item in enumerate(result, start=1):
        print(f"{i}. {item['text']}")

    try:
        choice = int(input("\nEnter the number of the topic you want to visit (or 0 to cancel): "))
        if choice == 0:
            return
        selected = result[choice - 1]
        selected_href = selected['href']
        selected_text = selected['text']
        browser.get(selected_href)  # Просто загружаем новую страницу
        time.sleep(5)
        # Теперь подсветим выбранный элемент
        browser.execute_script(f"""
            const links = Array.from(document.querySelectorAll('a'));
            const target = links.find(a => a.innerText.trim().replace(/^\\d+(\\.\\d+)*\\s*/, '') === `{selected_text}`);
            if (target) {{
                target.style.border = '3px solid yellow';
                target.style.backgroundColor = 'lightyellow';
                target.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}
        """)
    except (ValueError, IndexError):
        print("Invalid selection. Returning to the main menu.")
    try:
        choice = int(input("\nEnter the number of the link you want to open (or 0 to cancel): "))
        if choice == 0:
            return
        selected_link = good_links[choice - 1]
        selected_link.click()
        time.sleep(5)
    except (ValueError, IndexError):
        print("Invalid selection. Returning to the main menu.")


while True:
    print("\nWhat would you like to do?")
    print("1 - Browse the paragraphs of the current article")
    print("2 - Go to a related article")
    print("3 - Exit the program")
    action = input("Enter the number of your choice: ")

    if action == '1':
        list_paragraphs()
    elif action == '2':
        choose_link()
    elif action == '3':
        print("Exiting the program...")
        browser.quit()
        break
    else:
        print("Invalid input. Please try again.")
