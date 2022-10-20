import tensorflow




def make_input_fn(data_df, label_df, num_epochs = 10, shuffle = True, batch_size = 32): # Creates the input function.

	def input_funtion(): # Inner funtion which will  be returned.

		ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df)) # Create tf.data.Dataset object with data and its labels.

		if shuffle:

			ds = ds.shuffle(1000) # Randomize order of data.

		ds = ds.batch(batch_size).repeat(num_epochs) # Split dataset into batches of 32 and repeat process for number of epochs.
		
		return ds # Return a batch of the dataset.

	return input_funtion # Return a function object for use.
	
	trsin_input_fn = make_input_fn(dftrain, y_train) # Here we will call the input_function that was returned to us to get a dataset object.

	eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs = 1, shuffle = False) # False because we are not training it.

	#______________________________KEY NOTES_____________________________________

	# ds = dataset

	# tf = tensorframe

	# df = dataframe		


