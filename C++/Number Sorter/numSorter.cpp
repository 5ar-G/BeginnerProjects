#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

int main() {
    std::vector<double> numbers; 
    std::string input;

    while (true) {
        std::cout << "Enter a number (or 'q' to quit): ";
        std::cin >> input;

        if (input == "q" || input == "Q") {
            break;
        }

        try {
            double num = std::stod(input); 
            numbers.push_back(num);
        } catch (std::invalid_argument const &e) {
            std::cout << "Invalid input. Please enter a number or 'q' to quit." << std::endl;
        }
    }

    if (!numbers.empty()) {
        std::sort(numbers.begin(), numbers.end());
        std::cout<<"---------------------------------\n";

        std::cout << "Sorted numbers: ";
        for (double num : numbers) {
            if (num == static_cast<int>(num)) { 
                std::cout << static_cast<int>(num) << "   "; 
            } else {
                std::cout << std::fixed << std::setprecision(2) << num << " "; 
            }
        }
        std::cout << std::endl;
        std::cout<<"---------------------------------\n";
    } else {
        std::cout<<"---------------------------------\n";
        std::cout << "No numbers entered." << std::endl;
        std::cout<<"---------------------------------\n";
    }
    std::cout << "Press Enter to close the program.\n";
    std::cin.ignore(); // Ignore leftover input
    std::cin.get(); // Waits for the user to press Enter
    return 0;
   
}