#include <iostream>


int main(){
        double num1;
        double num2;
        char function;
    
        std::cout<<"1st number: ";
        std::cin>>num1;
        
        std::cout<<"2st number: ";
        std::cin>>num2;
       


        std::cout<<"What function you'd like to use(+, -, *, /): ";
        std::cin>>function;
        std::cout<<"--------------------------------\n";
        switch(function){
            case '+' : 
                std::cout<<num1<<"+"<<num2<<"="<<num1 + num2<<'\n';
                break;

            case '-' : 
                std::cout<<num1<<"-"<<num2<<"="<<num1 - num2<<'\n';
                break;

            case '*' : 
                std::cout<<num1<<"*"<<num2<<"= "<<num1 * num2<<'\n';
                break;

            case '/' : 
                std::cout<<num1<<"/"<<num2<<"="<<num1 / num2<<'\n';
                break;

            default: std::cout<<"Invalid input.\n";
        }
        std::cout<<"--------------------------------\n";
         std::cout << "Press Enter to close the program.\n";
        std::cin.ignore(); // Ignore leftover input
        std::cin.get(); // Waits for the user to press Enter

    return 0;
}