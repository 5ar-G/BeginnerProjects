#include <iostream>
#include <ctime>

void drawBoard(char *spaces){
    std::cout<<'\n';
    std::cout<< "     |     |     "<<'\n';
    std::cout<< "  "<<spaces[0]<<"  |  "<<spaces[1]<<"  |  "<<spaces[2]<<"  "<<'\n';
    std::cout<< "_____|_____|_____"<<'\n';
    std::cout<< "     |     |     "<<'\n';
    std::cout<< "  "<<spaces[3]<<"  |  "<<spaces[4]<<"  |  "<<spaces[5]<<"  "<<'\n';
    std::cout<< "_____|_____|_____"<<'\n';
    std::cout<< "     |     |     "<<'\n';
    std::cout<< "  "<<spaces[6]<<"  |  "<<spaces[7]<<"  |  "<<spaces[8]<<"  "<<'\n';
    std::cout<< "     |     |     "<<'\n';
    std::cout<<'\n';
}

void playerMove(char *spaces, char player) {
    int number;
    std::cout << "Enter spot to place " << player << "(1-9): ";
    std::cin >> number;
    while (number < 1 || number > 9) {
        std::cout << "Invalid input. Please enter a number between 1 and 9." << '\n';
        std::cout << "Enter spot to place " << player << "(1-9): ";
        std::cin >> number;
    }
    if (spaces[number - 1] != ' ') {
        std::cout << "Space already occupied. Please choose another space." << '\n';
        playerMove(spaces, player);
    } else {
        spaces[number - 1] = player;
    }
}

void computerMove(char *spaces, char computer){
    int number;
    srand(time(0));
    while(true){
        number = rand() % 9;
        if(spaces[number] == ' '){
            spaces[number] = computer;
            break;
        }
    }
}

bool checkWinner(char *spaces, char player, char computer){
    if((spaces[0] != ' ') && spaces[0] == spaces[1] && spaces[1] == spaces[2]){
        spaces[0] == player ? std::cout<<"---------------------------------\n"<<"You win!\n"<<"---------------------------------\n": std::cout<<"---------------------------------\n"<<"You lose!\n"<<"---------------------------------\n";
    }
    else if((spaces[3] != ' ') && spaces[3] == spaces[4] && spaces[4] == spaces[5]){
        spaces[3] == player ? std::cout<<"---------------------------------\n"<<"You win!\n"<<"---------------------------------\n": std::cout<<"---------------------------------\n"<<"You lose!\n"<<"---------------------------------\n";
    }
    else if((spaces[6] != ' ') && spaces[6] == spaces[7] && spaces[7] == spaces[8]){
        spaces[6] == player ? std::cout<<"---------------------------------\n"<<"You win!\n"<<"---------------------------------\n": std::cout<<"---------------------------------\n"<<"You lose!\n"<<"---------------------------------\n";
    }
    else if((spaces[0] != ' ') && spaces[0] == spaces[3] && spaces[3] == spaces[6]){
        spaces[0] == player ? std::cout<<"---------------------------------\n"<<"You win!\n"<<"---------------------------------\n": std::cout<<"---------------------------------\n"<<"You lose!\n"<<"---------------------------------\n";
    }
    else if((spaces[1] != ' ') && spaces[1] == spaces[4] && spaces[4] == spaces[7]){
        spaces[1] == player ? std::cout<<"---------------------------------\n"<<"You win!\n"<<"---------------------------------\n": std::cout<<"---------------------------------\n"<<"You lose!\n"<<"---------------------------------\n";
    }
    else if((spaces[2] != ' ') && spaces[2] == spaces[5] && spaces[5] == spaces[8]){
        spaces[2] == player ? std::cout<<"---------------------------------\n"<<"You win!\n"<<"---------------------------------\n": std::cout<<"---------------------------------\n"<<"You lose!\n"<<"---------------------------------\n";
    }
    else if((spaces[0] != ' ') && spaces[0] == spaces[4] && spaces[4] == spaces[8]){
        spaces[0] == player ? std::cout<<"---------------------------------\n"<<"You win!\n"<<"---------------------------------\n": std::cout<<"---------------------------------\n"<<"You lose!\n"<<"---------------------------------\n";
    }
    else if((spaces[2] != ' ') && spaces[2] == spaces[4] && spaces[4] == spaces[6]){
        spaces[2] == player ? std::cout<<"---------------------------------\n"<<"You win!\n"<<"---------------------------------\n": std::cout<<"---------------------------------\n"<<"You lose!\n"<<"---------------------------------\n";
    }
    else{
        return false;
    }
    return true;
}

bool checkTie(char *spaces){
    for(int i = 0; i<9; i++){
        if(spaces[i] == ' '){
            return false;
        }
    }
    std::cout<<"---------------------------------\n";
    std::cout<<"It's a tie!\n";
    std::cout<<"---------------------------------\n";
    return true;
}
int main(){
    char spaces[9] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
    char player = 'X';
    char computer = 'O';
    bool running = true;

    drawBoard(spaces);
    
    while(running){
        playerMove(spaces, player);
        computerMove(spaces, computer);
        drawBoard(spaces);
        if(checkWinner(spaces, player, computer)){
            running = false;
            break;
        }
        else if (checkTie(spaces)){
            running = false;
            break;
        }
    }
    std::cout<<"Thanks for playing.";
    std::cin.ignore(); // Ignore leftover input
    std::cin.get(); // Waits for the user to press Enter
    return 0;
}