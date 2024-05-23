def inch_swap(privatekey, amount_to_swap, to_token_address, to_symbol):
    """Swaps ETH for a token using 1inch.

    Args:
        privatekey (str): The private key of the account to use for the swap.
        amount_to_swap (float): The amount of ETH to swap.
        to_token_address (str): The address of the token to swap for.
        to_symbol (str): The symbol of the token to swap for.

    Returns:
        The transaction hash of the swap.
    """

    # Get the 1inch API key.
    api_key = os.environ.get("1INCH_API_KEY")

    # Get the 1inch client.
    client = Client(api_key)

    # Get the 1inch quote.
    quote = client.get_quote(
        from_token="ETH",
        to_token=to_token_address,
        amount=amount_to_swap,
    )

    # Get the 1inch swap transaction.
    swap_transaction = client.get_swap_transaction(
        quote=quote,
        private_key=privatekey,
    )

    # Send the 1inch swap transaction.
    transaction_hash = client.send_swap_transaction(
        swap_transaction=swap_transaction,
    )

    # Return the transaction hash.
    return transaction_hash
