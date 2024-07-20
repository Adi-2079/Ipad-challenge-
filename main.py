import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Year 9 Math App")

# Set up the font
font = pygame.font.Font(None, 36)

# Function to display the question and check the user's answer
def ask_question(question, answer):
    # Clear the screen
    screen.fill((255, 255, 255))

    # Display the question
    question_text = font.render(question, True, (0, 0, 0))
    question_rect = question_text.get_rect(center=(screen_width // 2, 50))
    screen.blit(question_text, question_rect)

    pygame.display.flip()

    # Wait for user's answer
    user_answer = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_answer
                elif event.key == pygame.K_BACKSPACE:
                    user_answer = user_answer[:-1]
                else:
                    user_answer += event.unicode

        # Clear the screen
        screen.fill((255, 255, 255))

        # Display the question and user's answer
        screen.blit(question_text, question_rect)

        answer_text = font.render(user_answer, True, (0, 0, 0))
        answer_rect = answer_text.get_rect(center=(screen_width // 2, 150))
        screen.blit(answer_text, answer_rect)

        pygame.display.flip()

# List of questions and answers
questions = [
    # Algebraic fraction questions
    ("Simplify the expression: (x + 2) / (x^2 - 4)", "1/x-2"),
    ("Solve for x: (2x + 5) / 3 = 4", "7/2"),
    ("Solve for x: x^2 plus 2x plus 1", "-1"),
    ("Expand the following: (x+4)(x+2)", "x^2 + 6x + 8"),
    ("Factorise the following: x^2 + 3x + 2", "(x+1)(x+2)"),
    # Add more algebraic fraction questions here

    # Trigonometry questions
    ("Find the value of sin(30 degrees)", "0.5"),
    ("What is the tangent of 45 degrees?", "1"),
    ("Find the hypotenuse if A = 3 and B = 4", "5"),
    ("What is the pythagorean theorem?", "a^2 + b^2 = c^2"),
    ("Find A if B = 12 and C = 13", "5"),

    # Add more trigonometry questions here

    # Rates and ratio questions
    ("If a car travels 300 miles in 5 hours, what is its speed?", "60"),
    ("How many hours will a car travelling at 120 km/h take to travel 360 km", "3"),
    # Add more rates and ratio questions here
]

# Start button class
class Button:
    def __init__(self, x, y, width, height, text, text_color, button_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.button_color = button_color
    
    def draw(self):
        pygame.draw.rect(screen, self.button_color, self.rect)
        
        button_text = font.render(self.text, True, self.text_color)
        button_text_rect = button_text.get_rect(center=self.rect.center)
        screen.blit(button_text, button_text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Start screen
def start_screen():
    start_button = Button(
        screen_width // 2 - 100,
        screen_height // 2 - 25,
        200,
        50,
        "Start",
        (255, 255, 255),
        (0, 0, 255)
    )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(event.pos):
                    return

        screen.fill((255, 255, 255))
        start_button.draw()
        pygame.display.flip()

# Pause menu
def pause_menu():
    resume_button = Button(
        screen_width // 2 - 100,
        screen_height // 2 - 50,
        200,
        50,
        "Resume",
        (255, 255, 255),
        (0, 0, 255)
    )
    quit_button = Button(
        screen_width // 2 - 100,
        screen_height // 2 + 50,
        200,
        50,
        "Quit",
        (255, 255, 255),
        (0, 0, 255)
    )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.is_clicked(event.pos):
                    return
                elif quit_button.is_clicked(event.pos):
                    return "QUIT"

        screen.fill((255, 255, 255))
        resume_button.draw()
        quit_button.draw()
        pygame.display.flip()

# End screen
def end_screen(correct_answers, total_questions):
    screen.fill((255, 255, 255))
    end_text = font.render("You answered {} out of {} questions correctly.".format(correct_answers, total_questions),
                           True, (0, 0, 0))
    end_rect = end_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    screen.blit(end_text, end_rect)
    
    restart_text = font.render("Press ENTER to restart", True, (0, 0, 0))
    restart_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

# Main game loop
def game_loop():
    correct_answers = 0
    
    # Loop through the questions
    for question, answer in questions:
        # Ask the question
        user_answer = ask_question(question, answer)
        
        # Check if the user wants to pause the game
        if user_answer == "PAUSE":
            pause_result = pause_menu()
            if pause_result == "QUIT":
                return

        # Check the answer
        if user_answer == answer:
            feedback = "Correct!"
            correct_answers += 1
        else:
            feedback = "Incorrect. The correct answer is " + answer

        # Display feedback and correct answer
        screen.fill((255, 255, 255))
        feedback_text = font.render(feedback, True, (0, 0, 0))
        feedback_rect = feedback_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        screen.blit(feedback_text, feedback_rect)

        correct_answer_text = font.render("The correct answer is " + answer, True, (0, 0, 0))
        correct_answer_rect = correct_answer_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(correct_answer_text, correct_answer_rect)
        pygame.display.flip()

        time.sleep(2)  # Pause for 2 seconds
    
    # Show the end screen
    end_screen(correct_answers, len(questions))

# Run the app
while True:
    start_screen()
    game_loop()