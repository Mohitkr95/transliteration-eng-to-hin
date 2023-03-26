import tensorflow as tf
import numpy as np

def predict_target_name(model_path, source_name, max_source_length, source_chars, source_char_to_int, max_target_length, target_chars, target_int_to_char, target_char_to_int):
    # load the saved model
    model = tf.keras.models.load_model(model_path)

    # encode the source name
    encoder_input_data = np.zeros((1, max_source_length, len(source_chars)), dtype='float32')
    for j, char in enumerate(source_name):
        if char in source_char_to_int:
            encoder_input_data[0, j, source_char_to_int[char]] = 1.0
    
    # perform inference
    decoder_input_data = np.zeros((1, max_target_length + 1, len(target_chars)), dtype='float32')
    decoder_input_data[0, 0, target_char_to_int['\t']] = 1.0 # set the first input character as the start-of-sequence token
    output = model.predict([encoder_input_data, decoder_input_data])[0]
    
    # decode the output to obtain the predicted target name
    predicted_target_name = ''
    for i in range(max_target_length):
        char_index = np.argmax(output[i])
        char = target_int_to_char[char_index]
        if char == '\n': # stop decoding if the end-of-sequence token is generated
            break
        predicted_target_name += char
    
        # update the input for the next time step
        decoder_input_data[0, i+1, char_index] = 1.0
    
    return predicted_target_name
