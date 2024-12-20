#include <iostream>
#include <string>

// Function to extract the username and domain from an email address
void emailSlicer(const std::string& email) {
    size_t atPos = email.find('@');
    if (atPos != std::string::npos) {
        std::string username = email.substr(0, atPos);
        std::string domain = email.substr(atPos + 1);
        std::cout << "Username: " << username << std::endl;
        std::cout << "Domain: " << domain << std::endl;
    } else {
        std::cerr << "Invalid email address." << std::endl;
    }
}

int main() {
    std::string email;
    std::cout << "Enter an email address: ";
    std::cin >> email;
    emailSlicer(email);
    std::cout << "Press Enter to close the program.\n";
    std::cin.ignore(); // Ignore leftover input
    std::cin.get(); // Waits for the user to press Enter
    return 0;
}