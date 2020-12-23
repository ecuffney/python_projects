import random
import words


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    while index < len(template):
        if template[index:index+8] == '{{noun}}':
            # Add a random noun to the output.
            output.append(random.choice(nouns))
            index += 8
        elif template[index:index+8] == '{{verb}}':
            # Add a random verb to the output.
            output.append(random.choice(verbs))
            index += 8
        else:
            # Copy a character to the output.
            output.append(template[index])
            index += 1

    # Join the output into a single string.
    output = ''.join(output)

    return output


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))
