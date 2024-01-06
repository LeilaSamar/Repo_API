{[200~import logging

logging.basicConfig(level=logging.DEBUG)

def say_hello(name: str, repeat: int = 1, goodbye: bool = False) -> None:
    try:
        if goodbye:
            message = 'Goodbye'
        else:
            message = 'Hello'
            
        for _ in range(repeat):
            logging.debug(f'{message} {name}!')
            
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')

say_hello('World')

say_hello('World', 3, True)~}
