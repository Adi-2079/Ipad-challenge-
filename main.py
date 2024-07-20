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

