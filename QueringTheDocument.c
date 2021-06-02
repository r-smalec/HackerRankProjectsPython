#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX_CHARACTERS 1005
#define MAX_PARAGRAPHS 5
#define MAX_WORDS 20
#define MAX_SENTENCES 20

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
    
    char**** doc = (char****)malloc(MAX_PARAGRAPHS * sizeof(char***));

    for (int p = 0; p < MAX_PARAGRAPHS; p++) {
            *(doc + p) = (char***)malloc(MAX_SENTENCES * sizeof(char**));

            for (int s = 0; s < MAX_SENTENCES; s++) {
                    *(*(doc + p) + s) = (char**)malloc(MAX_WORDS * sizeof(char*));

                    for (int w = 0; w < MAX_WORDS; w++) {
                            *(*(*(doc + p) + s) + w) = (char*)malloc(MAX_CHARACTERS * sizeof(char));
                    }
            }
    }
    
    char* pSen;
    char* pPrevSen = text;
    char* pWord;
    char* pPrevWord;

    int parCurrent = 0;
    int senCurrent = 0;
    int wordCurrent = 0;

    do {
        pSen = strchr(pPrevSen, '.');
        char* sentence = (char*)calloc(MAX_WORDS * MAX_CHARACTERS, sizeof(char));
        strncpy(sentence, pPrevSen, (size_t)(pSen + 1 - pPrevSen));
        sentence = realloc(sentence, strlen(sentence));
        pPrevWord = sentence;
        //printf("%s\n", sentence);

        wordCurrent = 0;

            do {
                    pWord = strchr(pPrevWord, ' ');

                    if(pWord == NULL) {

                        pWord = strchr(pPrevWord, '.');
                        if(pWord == NULL)
                            break;
                    }
                    
                    char* word = (char*)calloc((int)(MAX_CHARACTERS / MAX_WORDS), sizeof(char));
                    strncpy(word, pPrevWord, (size_t)(pWord - pPrevWord));
                    word = realloc(word, strlen(word));
                    //printf("%s %d %d %d\n", word, parCurrent, senCurrent, wordCurrent);
                    strcpy(*(*(*(doc + parCurrent) + senCurrent) + wordCurrent), word);
                    *(*(*(doc + parCurrent) + senCurrent) + wordCurrent) = realloc(*(*(*(doc + parCurrent) + senCurrent) + wordCurrent), strlen(word));

                    wordCurrent++;
                    pPrevWord = pWord + 1;
                    free(word);

            } while(*(pPrevWord) != '.');

        senCurrent++;
        pPrevSen = pSen + 1;
        free(sentence);

        if(*(pPrevSen) == '\n') {
            pPrevSen += 1;
            parCurrent++;
            senCurrent = 0;
        }

    } while(strchr(pPrevSen, '.') != NULL);

    return doc;
}

int main() {

    char* text = "Ala ma kota.Kot ma Ale.\nAla ma kurwice, wiec wypila soplice.";
    //char* text = "Ma ma ma ma ma ma.Be be be be, be be.";

    char**** doc = get_document(text);
    printf("%s", kth_word_in_mth_sentence_of_nth_paragraph(doc, 1, 1, 1));
    free(doc);
    return 0;
}
