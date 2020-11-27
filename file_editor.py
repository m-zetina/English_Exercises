import os
import pickle


def define(vocab_dict):
    inp = input('define > ')
    if ':' in inp:
        vocab, translation = inp.split(':')
        vocab_dict.setdefault(vocab, [])
        vocab_dict[vocab].append(translation.rstrip().lstrip())
        print(f'    out > {inp}\n')

    else:
        raise ValueError("Incorrect input for define! Use 'defintion: translation' instead!")


def remove(vocab_dict, defintion=False):
    inp = input('remove > ')
    if defintion:
        key, translation = inp.split(':')
    else:
        key = inp

    if key in vocab_dict:
        if not defintion:
            vocab_dict.pop(key)
            print('    out > Deleted!\n')
        
        else:
            vocab_dict[key].remove(translation.rstrip().lstrip())
            print(f'    out > Deleted {translation.rstrip().lstrip()} from {key}!\n')

    else:
        raise NameError(f'{inp} is not in dictionary')

def remove_from(vocab_dict):
    return remove(vocab_dict, True)


def find_words_with(vocab_dict):
    inp = input('find > ')
    found_words = set()
    for key in vocab_dict:
        if inp in key:
            found_words.add(key)

    if found_words:
        print(f'    out > Found: {found_words}\n')
    else:
        print(f'    out > No words/phrases containing {inp} were found!\n')


def print_dict(vocab_dict):
    if vocab_dict:
        print('    out > ')
        for vocab, translation in vocab_dict.items():
            translation = ';'.join(translation) if len(translation) > 1 else translation[0]
            print(f'         {vocab}: {translation}')
    else:
        print('   out > ')


def is_valid_input(inp):
    if inp.lower() in actions:
        return actions[inp]
        
    raise ValueError(f"Invalid action! Use one of the following actions: {', '.join(actions)}.")


def confirm_input(vocab, translation):
    confirmation = input(f'This was the input: "{vocab}: {translation}", confirm? y or n\n')
    return confirmation == 'y'


def repl():
    vocab_dict = {}
    files = get_files()
    filename = input(f"Create a new file format or select from an existing one: {', '.join(files)}, type in 'filename.pickle' format \n")
    init_pickle_file(filename)

    stored_vocab = unserialize_data(filename)
    vocab_dict.update(stored_vocab)
    while True:
        inp = input('in > ').rstrip()
        if inp in ['done', 'quit', 'exit']:
            serialize_data(vocab_dict, filename)
            break

        if inp in ['change', 'switch']:
            serialize_data(vocab_dict, filename)
            vocab_dict = {}
            repl()
            break

        try:
            func = is_valid_input(inp)
            func(vocab_dict)

        except Exception as e:
            print(f'  Error: {e}')


actions = {
    'add': define,
    'define': define,
    'delete': remove,
    'remove': remove,
    'remove from': remove_from,
    'view': print_dict,
    'print': print_dict,
    'find': find_words_with,
    'search': find_words_with,
}


def serialize_data(data, filename):
    with open(f'pickles/{filename}', 'wb') as f:
        pickle.dump(data, f)


def unserialize_data(filename):
    """
    Returns the stored dictionary of vocabulary given the filename in 
    'filename.pickle' format (filename must be a string).
    """
    with open(f'pickles/{filename}', 'rb') as f:
        stored_vocab = pickle.load(f)
    
    return stored_vocab


def init_pickle_file(filename):
    files = os.listdir('./pickles')
    if filename not in files:
        with open(f'pickles/{filename}', 'wb') as f:
            pickle.dump({}, f)


def get_files():
    files = os.listdir('./pickles')
    return files


if __name__ == "__main__":
    repl()
    pass