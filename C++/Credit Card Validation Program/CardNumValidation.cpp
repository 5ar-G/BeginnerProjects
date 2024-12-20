#include <iostream>

int getDigit(const int number){
    return number % 10 + (number / 10 % 10);
}
int sumEvenDigits(const std::string cardNum){
    int sum= 0;
    for(int i = cardNum.size() - 2; i>=0; i-=2 ){
        sum += getDigit((cardNum[i] - '0') * 2);
    }
    return sum;
}
int sumOddDigits(const std::string cardNum){
    int sum= 0;
    for(int i = cardNum.size() - 1; i>=0; i-=2 ){
        sum += cardNum[i] - '0';
    }
    return sum;
}




int main(){

    std::string cardNum;
    int result =0;
    std::cout<<"Enter a credit card number: ";
    std::getline(std::cin, cardNum);

    result = sumEvenDigits(cardNum) + sumOddDigits(cardNum);

    if(result % 10 == 0){
        std::cout<<"--------------------------------------------------\n";
        std::cout<<"Your number: "<<cardNum<<" is valid.\n";
        std::cout<<"--------------------------------------------------\n";
    }
    else{
        std::cout<<"--------------------------------------------------\n";
        std::cout<<"Your number: "<<cardNum<<" is not valid.\n";
        std::cout<<"--------------------------------------------------\n";
    }
    std::cout << "Press Enter to close the program.\n";
    std::cin.ignore(); // Ignore leftover input
    std::cin.get(); // Waits for the user to press Enter
    return 0;
}