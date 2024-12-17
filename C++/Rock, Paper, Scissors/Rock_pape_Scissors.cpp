#include <iostream>
#include <cstdlib>
#include <ctime>
#include <limits> // For std::numeric_limits

char getUserChoice() {
    char player;
    std::cout << "************ Rock, Paper, Scissors Game ************\n\n";

    do {
        std::cout << "--------------------------\n";
        std::cout << "1. Rock\n";
        std::cout << "2. Paper\n";
        std::cout << "3. Scissors\n";
        std::cout << "Choose (1-3): ";
        std::cin >> player;

        // Input validation: ensure it's one of '1', '2', or '3'
        if (std::cin.fail() || (player != '1' && player != '2' && player != '3')) {
            std::cin.clear(); // Clear the error flag
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); // Discard invalid input
            std::cout << "Invalid choice! Please try again.\n";
        } else {
            break; // Valid input, exit the loop
        }
    } while (true);

    return player;
}

char getComputerChoice() {
    srand(static_cast<unsigned int>(time(0))); // Seed the random number generator
    int num = (rand() % 3) + 1;
    switch (num) {
        case 1: return '1';
        case 2: return '2';
        case 3: return '3';
    }
    return 0;
}

void showChoice(char choice) {
    switch (choice) {
        case '1': std::cout << "Rock\n"; break;
        case '2': std::cout << "Paper\n"; break;
        case '3': std::cout << "Scissors\n"; break;
    }
}

void chooseWinner(char player, char computer) {
    if (player == computer) {
        std::cout << "It is a draw!\n";
    } else if ((player == '1' && computer == '3') ||
               (player == '2' && computer == '1') ||
               (player == '3' && computer == '2')) {
        std::cout << "Player wins!\n";
    } else {
        std::cout << "Computer wins!\n";
    }
}

int main() {
    char player = getUserChoice();
    char computer = getComputerChoice();

    std::cout << "-------------------------\n";
    std::cout << "Player's choice: ";
    showChoice(player);
    std::cout << "Computer's choice: ";
    showChoice(computer);
    std::cout << "-------------------------\n";
    chooseWinner(player, computer);
    std::cout << "-------------------------\n";

    std::cout << "Press Enter to close the program.\n";
    std::cin.ignore(); // Ignore leftover input
    std::cin.get(); // Waits for the user to press Enter
    return 0;
}
