#include <iostream>

int main(){
    double temp;
    char unit;

    std::cout<<"Enter your temp: ";
    std::cin>>temp;


    std::cout<<"Is this in Celsius or Kelvin(C/K): ";
    std::cin>>unit;

 
        if('C' || 'c') {
            temp += 273.15; 
            std::cout<<"That is: "<<temp<<"K\n";
        }
            
        
        else if('K' || 'k'){
            temp -= 273.15;
            std::cout<<"That is: "<<temp<<"C\n";
        }
            
        else{
            std::cout<<"Invalid input\n";
        } 
            
            
        std::cout << "Press Enter to close the program.\n";
        std::cin.ignore(); // Ignore leftover input
        std::cin.get(); // Waits for the user to press Enter
      

    return 0;
}