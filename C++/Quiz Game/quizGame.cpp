#include <iostream>

int main(){
    std::string questions[]= {"What are you?","What is your name?","How old are you?","Where were you born?"};
    std::string options[][3]= {{"A: Man", "B: Woman", "C:AI"},
                                {"A: Petar", "B: Josip", "C: Luka"},
                                {"A: <18", "B: 18", "C: >18"},
                                {"A: RH", "B: RS", "C: B&H"}};
    
    char answers[] = {'A', 'A', 'B', 'C'};
    char guesses;
    double score= 0;
    int size = sizeof(questions) / sizeof(questions[0]);

    for(int i = 0; i<size; i++){
        std::cout<<"---------------------------\n";
        std::cout<< questions[i]<<'\n';
        std::cout<<"---------------------------\n";

        for(int j = 0; j < sizeof(options[i]) / sizeof(options[i][0]); j++ ){
            std::cout<<options[i][j]<<'\n';
        }
        std::cin>>guesses;
        guesses = toupper(guesses);

        if(guesses == answers[i]){
            std::cout<<"CORRECT!\n";
            score++;
        }
        else{
            std::cout<<"WRONG!\n";
            std::cout<<"The asnwer was: "<<answers[i]<<'\n';
        }
    }
    std::cout<<"______________________________\n";
    std::cout<<"         FINAL RESULTS        \n";
    std::cout<<"______________________________\n";
    std::cout<<"Total questions: "<<size<<'\n';
    std::cout<<"Correct answers: "<<score<<" \n";
    std::cout<<"Your score: "<<(score/(double)size)*100<<"%\n";
    std::cin.ignore(); // Ignore leftover input
    std::cin.get(); // Waits for the user to press Enter
    return 0;
}
