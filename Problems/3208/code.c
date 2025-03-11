#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int repeated_color_index_founder(int* group, int size) {
    for (int i = 1; i < size; i++) {
        if (group[i] == group[i - 1]) {
            return i;
        }
    }
    return -1;
}

int numberOfAlternatingGroups(int* colors, int colorsSize, int k) {
    if (colorsSize == 0 || k <= 0) return 0;
    
    int* line_of_combinations = (int*)malloc((colorsSize + k - 1) * sizeof(int));
    for (int i = 0; i < colorsSize; i++) {
        line_of_combinations[i] = colors[i];
    }
    for (int i = 0; i < k - 1; i++) {
        line_of_combinations[colorsSize + i] = colors[i];
    }
    
    int number_of_alternating_groups = 0;
    int skip_to = 0;
    bool was_previous_group_alternating = false;
    
    for (int index = 0; index < colorsSize; index++) {
        if (index >= skip_to) {
            int* group = &line_of_combinations[index];
            
            if (!was_previous_group_alternating) {
                int repeated_color_index = repeated_color_index_founder(group, k);
                if (repeated_color_index != -1) {
                    skip_to = index + repeated_color_index;
                    was_previous_group_alternating = false;
                } else {
                    number_of_alternating_groups++;
                    was_previous_group_alternating = true;
                }
            } else {
                if (group[k - 1] == group[k - 2]) {
                    was_previous_group_alternating = false;
                } else {
                    number_of_alternating_groups++;
                }
            }
        }
    }
    
    free(line_of_combinations);
    return number_of_alternating_groups;
}