#include <iostream>
#include <limits>

int balance = 100;

void withdraw(){
   int withdraw_value;
   std::cout<<"Enter amount to withdraw: ";
   std::cin>>withdraw_value;
    if (std::cin.fail() || withdraw_value <= 0) {
        std::cin.clear(); 
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Invalid input. Please enter a positive amount.\n";
        return;
    }

    if (withdraw_value > balance) {
        std::cout << "Insufficient funds. Your balance is: " << balance << "$\n";
    } else {
        balance -= withdraw_value;
        std::cout << "Withdrawal successful. Your new balance is: " << balance << "$\n";
    }
}
void deposit(){
   int deposit_value;
   std::cout<<"Enter amount to deposit: ";
   std::cin>>deposit_value;
  
    if (std::cin.fail() || deposit_value <= 0) {
        std::cin.clear(); 
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
        std::cout << "Invalid input. Please enter a positive amount.\n";
        return;
    }

    balance += deposit_value;
    std::cout << "Deposit successful. Your new balance is: " << balance << "$\n";
}
void show_balance(){
    std::cout<<"Your balance is: "<<balance<<"$"<<'\n';
}


int main(){
    int choice = 0;
    do{
        std::cout<<"----------------ATM----------------\n\n";
        std::cout<<"1. Show balance\n";
        std::cout<<"2. Withdraw\n";
        std::cout<<"3. Deposit\n";
        std::cout<<"4. Exit\n";
        std::cout<<"--------------------------------------\n";
        std::cout<<"Chose function(1-4): ";
        std::cin>>choice;

        if (std::cin.fail()) {
            std::cin.clear(); 
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); 
            std::cout << "Invalid input. Please enter a number between 1 and 4.\n";
            continue;
        }

        switch(choice){
            case 1: show_balance();
                    break;
            case 2: withdraw();
                    break;
            case 3: deposit();
                    break; 
            case 4: std::cout<<"Thanks for visiting.\n";
                    break;
            default: std::cout<<"Invalid choice! Please try again.\n";
                    break;

        }
    }while(choice != 4);
    return 0;
}
