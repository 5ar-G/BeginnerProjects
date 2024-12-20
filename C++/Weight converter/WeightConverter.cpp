#include <iostream>

int main(){
    double weight;
    char unit;

    std::cout<<"Enter your Weight: ";
    std::cin>>weight;


    std::cout<<"Is this in Kg or Lb(K/L): ";
    std::cin>>unit;

 
        if('K' || 'k') {
            weight = weight * 2.2046;
            std::cout<<"That is: "<<weight<<"lb\n";
        }
            
        
        else if('L' || 'l'){
            weight = weight * 2.2046;
            std::cout<<"That is: "<<weight<<"kg\n";
        }
            
        else{
            std::cout<<"Invalid input\n";
        } 
            
            
        std::cout << "Press Enter to close the program.\n";
        std::cin.ignore(); // Ignore leftover input
        std::cin.get(); // Waits for the user to press Enter
      

    return 0;
}