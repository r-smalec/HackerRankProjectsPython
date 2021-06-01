#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5
#define MAX_WORDS 15
#define MAX_SENTENCES 15

char* kth_word_in_mth_sentence_of_nth_paragraph(char**** document, int k, int m, int n) {
    
    return document[n - 1][m - 1][k - 1];
}

char** kth_sentence_in_mth_paragraph(char**** document, int k, int m) { 
    
    return document[m - 1][k - 1];
}

char*** kth_paragraph(char**** document, int k) {
    
    return document[k - 1];
}

char**** get_document(char* text) {
    
    char**** document = (char****)malloc(MAX_PARAGRAPHS * sizeof(char***));
    
    for(int i = 0; i < MAX_PARAGRAPHS; i++) {
        *(document + i) = (char***)malloc(MAX_SENTENCES * sizeof(char**));
        
        for(int j = 0; j < MAX_WORDS; j++) {
            *(*(document + i) + j) = (char**)malloc(MAX_WORDS * sizeof(char*));
            
            for(int k = 0; k < MAX_CHARACTERS; k++) {
                *(*(*(document + i) + j) + k) = (char*)malloc(MAX_CHARACTERS * sizeof(char));
            }
        }
    }
    
    char* p = strchr(text, '.');
    char* sentence;
    strncpy(sentence, text, p - text);

    char* word;
    int iPrev = 0;

    for(int i = 0; i < strlen(p); i++) {

        if( *(p + i) == ' ') {
            
            strncpy(word, (p + iPrev), i - iPrev);
        }

        iPrev = i;
    }

    return document;
}

int main() {

    char* text = "Ala ma kota.Kot ma Ale\nAla ma kurwice wiec wypila soplice.";
    char* pPrevSen = text;
    char* pPrevWord;

    int parCurrent = 0;
    int senCurrent = 0;
    int wordCurrent = 0;


    do {
        char* pSen = strchr(pPrevSen, '.');
        char* sentence = (char*)malloc(MAX_WORDS * MAX_CHARACTERS * sizeof(char));
        strncpy(sentence, pPrevSen, (size_t)(pSen - pPrevSen));
        sentence = realloc(sentence, strlen(sentence));
        printf("%s\n", sentence); //TODO pyntla do obsługi podziału na słowa, przypisanie słów do document

            do {
                    char* pWord = strchr(pPrevWord, ' ');
                    char* word = (char*)malloc(MAX_CHARACTERS * sizeof(char));
                    strncpy(word, pPrevWord, (size_t)(pWord - pPrevWord));
                    word = realloc(word, strlen(word));

            } while(*(pPrevWord) != '.');

        senCurrent++;

        pPrevSen = pSen + 1;
        if(*(pPrevSen) == '\n') {
            pPrevSen += 1; //TODO iterowanie pyntli dla kolejnego akapitu
            parCurrent++;
        }
            
    } while(strchr(pPrevSen, '.') != NULL);
    
    //char**** document = get_document(text);

    
    //printf("%s", kth_word_in_mth_sentence_of_nth_paragraph(document, 0, 1, 1));
    //free(document);
    return 0;
}
