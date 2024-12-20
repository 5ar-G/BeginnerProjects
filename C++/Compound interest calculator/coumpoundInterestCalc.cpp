#include <iostream>
#include <cmath>


int main (){
    double principle;
    double rate;
    int time;

    std::cout<<"Enter principle amount: ";
    std::cin>>principle;

    if(principle < 0){
        std::cout<<"Principle cant be below 0.\n";
        exit(0);
    }

    std::cout<<"Enter rate amount: ";
    std::cin>>rate;

    if(rate < 0){
        std::cout<<"Rate cant be below 0.\n";
        exit(0);
    }

    std::cout<<"Enter time amount: ";
    std::cin>>time;

    if(time < 0){
        std::cout<<"Time cant be below 0.\n";
        exit(0);
    }
    if(!(std::cin >> time)) {
        std::cout << "Invalid input. Please enter a valid integer value for the time period!\n";
        exit(0);
        exit(0);
    }
    double total = principle * pow((1 + rate / 100), time);
    std::cout<<"--------------------------------\n";
    std::cout<<"Your total is: "<<total<<".\n";
    std::cout<<"--------------------------------\n";
    std::cout << "Press Enter to close the program.\n";
    std::cin.ignore(); // Ignore leftover input
    std::cin.get(); // Waits for the user to press Enter
}