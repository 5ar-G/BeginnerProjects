#include <iostream>
#include <iomanip>
#include <map>
#include <vector>
#include <string>
using namespace std;

int main() {
    // Menu initialization
    map<string, double> menu = {
        {"pizza", 2.46}, {"cookies", 1.73}, {"pancake", 4.6}, {"waffle", 5.0},
        {"popcorns", 4.56}, {"nachos", 3.0}, {"fries", 2.50}, {"water", 2.0},
        {"coke", 3.6}, {"sprite", 3.0}
    };

    vector<string> cart;
    double total = 0.0;

    // Display menu
    cout << "----------MENU----------" << endl;
    for (const auto& [key, value] : menu) {
        cout << setw(10) << left << key << ": $" << fixed << setprecision(2) << value << endl;
    }
    cout << "------------------------" << endl;

    // User input loop
    while (true) {
        cout << "Select item (Q to quit): ";
        string food;
        getline(cin, food);

        // Convert to lowercase
        for (char& c : food) c = tolower(c);

        if (food == "q") {
            break;
        } else if (menu.find(food) != menu.end()) {
            cart.push_back(food);
        } else {
            cout << "Item not found in the menu. Please try again." << endl;
        }
    }

    // Display order summary
    cout << "----------ORDER----------" << endl << endl;
    for (const string& food : cart) {
        total += menu[food];
        cout << setw(10) << left << food << ": $" << fixed << setprecision(2) << menu[food] << endl;
    }
    cout << endl;
    cout << "Your total is: $" << fixed << setprecision(2) << total << endl;
    cout << "------------------------" << endl;

    return 0;
}
