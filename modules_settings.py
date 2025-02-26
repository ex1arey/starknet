import asyncio

from modules import *


async def deposit_starknet(_id, key, type_account, recipient):
    """
    Deposit to Starknet
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    all_amount = True

    min_percent = 500
    max_percent = 500

    bridge = Bridge(_id, key, type_account, recipient)
    await bridge.deposit(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def withdraw_starknet(_id, key, type_account, recipient):
    """
    Withdraw from Starknet
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    min_amount = 0.019
    max_amount = 0.02
    decimal = 5

    all_amount = False

    min_percent = 5
    max_percent = 5

    bridge = Starknet(_id, key, type_account)
    await bridge.withdraw(recipient, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_orbiter(_id, key, type_account, recipient):
    """
    Bridge on Orbiter
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_chain = "arbitrum"
    to_chain = "starknet"

    min_amount = 0.005
    max_amount = 0.006
    decimal = 5

    all_amount = False

    min_percent = 2
    max_percent = 5

    bridge = Orbiter(_id, key, type_account, recipient)
    await bridge.bridge(from_chain, to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_avnu(_id, key, type_account):
    """
    Make swap on Avnu
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC, DAI | Select one
    to_token – Choose DESTINATION token ETH, USDC, DAI | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDT"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 4
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    avnu = Avnu(_id, key, type_account)
    await avnu.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_jediswap(_id, key, type_account):
    """
    Make swap on Jediswap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC, DAI | Select one
    to_token – Choose DESTINATION token ETH, USDC, DAI | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDT"
    to_token = "ETH"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    jediswap = Jediswap(_id, key, type_account)
    await jediswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_myswap(_id, key, type_account):
    """
    Make swap on MySwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC, DAI | Select one
    to_token – Choose DESTINATION token ETH, USDC, DAI | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDT"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 5
    max_percent = 10

    myswap = MySwap(_id, key, type_account)
    await myswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_starkswap(_id, key, type_account):
    """
    Make swap on 10kSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC, DAI | Select one
    to_token – Choose DESTINATION token ETH, USDC, DAI | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDT"
    to_token = "ETH"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    starkswap = StarkSwap(_id, key, type_account)
    await starkswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_sithswap(_id, key, type_account):
    """
    Make swap on SithSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC, DAI | Select one
    to_token – Choose DESTINATION token ETH, USDC, DAI | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDT"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 5
    max_percent = 10

    sithswap = SithSwap(_id, key, type_account)
    await sithswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_protoss(_id, key, type_account):
    """
    Make swap on Protoss
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDC, DAI | Select one
    to_token – Choose DESTINATION token ETH, USDC, DAI | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDT"
    to_token = "ETH"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    protoss = Protoss(_id, key, type_account)
    await protoss.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def deposit_zklend(_id, key, type_account):
    """
    Make deposit on ZkLend
    ______________________________________________________
    use_token – random choice token for deposit ["ETH", "DAI", "USDC"], you can use only one token ["ETH"]
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """

    use_token = ["ETH"]

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 20
    sleep_to = 120

    make_withdraw = True

    all_amount = True

    min_percent = 10
    max_percent = 50

    zklend = ZkLend(_id, key, type_account)
    await zklend.deposit(
        use_token, min_amount, max_amount, decimal, sleep_from,
        sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def withdraw_zklend(_id, key, type_account):
    """
    Make withdraw from ZkLend
    ______________________________________________________
    use_token – random choice token for withdraw ["ETH", "DAI", "USDC"], you can use only one token ["ETH"]
    """

    use_token = ["ETH", "DAI", "USDC"]

    zklend = ZkLend(_id, key, type_account)
    await zklend.withdraw_all(use_token)


async def enable_collateral_zklend(_id, key, type_account):
    """
    Enable collaterl on ZkLend
    ______________________________________________________
    use_token – random choice token for withdraw ["ETH", "DAI", "USDC"], you can use only one token ["ETH"]
    """

    use_token = ["ETH", "DAI", "USDC"]

    zklend = ZkLend(_id, key, type_account)
    await zklend.enable_collateral(use_token)


async def disable_collateral_zklend(_id, key, type_account):
    """
    Disable collateral on ZkLend
    ______________________________________________________
    use_token – random choice token ["ETH", "DAI", "USDC"], you can use only one token ["ETH"]
    """

    use_token = ["DAI"]

    zklend = ZkLend(_id, key, type_account)
    await zklend.disable_collateral(use_token)


async def make_transfer(_id, key, type_account, recipient):
    """
    Transfer ETH
    """

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    all_amount = True

    min_percent = 5
    max_percent = 10

    transfer = Transfer(_id, key, type_account, recipient)
    await transfer.transfer_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_multiswap(_id, key, type_account):
    """
    Multi-Swap module: Automatically performs the specified number of swaps in one of the dexes.
    ______________________________________________________
    use_dex - Choose any dex: jediswap, myswap, 10kswap, sithswap, protoss, avnu
    quantity_swap - Quantity swaps
    ______________________________________________________
    random_swap_token - If True the swap path will be [ETH -> USDC -> USDC -> ETH] (random!)
    If False the swap path will be [ETH -> USDC -> ETH -> USDC]
    """

    use_dex = ["jediswap", "myswap", "10kswap", "sithswap", "protoss", "avnu"]

    min_swap = 1
    max_swap = 3

    sleep_from = 150
    sleep_to = 500

    slippage = 2

    random_swap_token = True

    min_percent = 10
    max_percent = 60

    multi = Multiswap(_id, key, type_account)
    await multi.swap(
        use_dex, sleep_from, sleep_to, min_swap, max_swap, slippage, random_swap_token, min_percent, max_percent
    )


async def swap_tokens(_id, key, type_account):
    """
    SwapTokens module: Automatically swap tokens to ETH
    ______________________________________________________
    use_dex - Choose any dex: jediswap, myswap, 10kswap, sithswap, protoss, avnu
    """

    use_dex = ["jediswap", "myswap", "10kswap", "sithswap", "protoss", "avnu"]

    tokens = ["USDC", "DAI"]

    sleep_from = 200
    sleep_to = 800

    slippage = 2

    min_percent = 100
    max_percent = 100

    multi = SwapTokens(_id, key, type_account)
    await multi.swap(use_dex, tokens, sleep_from, sleep_to, slippage, min_percent, max_percent)


async def custom_routes(account_id, key, type_account):
    """
    swap_jediswap, swap_myswap, swap_starkswap, swap_sithswap, swap_protoss, swap_avnu,
    deposit_zklend, withdraw_zklend, enable_collateral_zklend, disable_collateral_zklend,
    mint_starknet_id, mint_starkverse, send_mail_dmail,
    swap_multiswap
    ______________________________________________________
    Disclaimer - You can add modules to [] to select random ones,
    example [module_1, module_2, [module_3, module_4], module 5]
    The script will start with module 1, 2, 5 and select a random one from module 3 and 4
    """
    """
        BRIDGE:
            – deposit_starknet
            – withdraw_starknet
            – bridge_orbiter
        DEX:
            – swap_jediswap
            – swap_myswap
            – swap_starkswap
            – swap_sithswap
            – swap_protoss
            – swap_avnu
        LANDING:
            – deposit_zklend
            – withdraw_zklend
            – enable_collateral_zklend
            – disable_collateral_zklend
        NFT/DOMAIN:
            – mint_starknet_id
            – mint_starkverse
        ANOTHER:
            – send_mail_dmail
            – swap_tokens
            – swap_multiswap
            – make_transfer
        ______________________________________________________
        Disclaimer - You can add modules to [] to select random ones,
        example [module_1, module_2, [module_3, module_4], module 5]
        The script will start with module 1, 2, 5 and select a random one from module 3 and 4
        """

    use_modules = [deposit_zklend, deposit_zklend, deposit_zklend, deposit_zklend]

    sleep_from = 1
    sleep_to = 3

    random_module = True

    routes = Routes(account_id, key, type_account)
    await routes.start(use_modules, sleep_from, sleep_to, random_module)


#########################################
########### NO NEED TO CHANGE ###########
#########################################

async def mint_starknet_id(_id, key, type_account):
    starknet_id = StarknetId(_id, key, type_account)
    await starknet_id.mint()


async def send_mail_dmail(_id, key, type_account):
    dmail = Dmail(_id, key, type_account)
    await dmail.send_mail()


async def mint_starkverse(_id, key, type_account):
    starkverse = StarkVerse(_id, key, type_account)
    await starkverse.mint()


async def create_collection_pyramid(_id, key, type_account):
    pyramid = Pyramid(_id, key, type_account)
    await pyramid.mint()


async def cancel_order_unframed(_id, key, type_account):
    unframed = Unframed(_id, key, type_account)
    await unframed.cancel_order()


async def cancel_order_flex(_id, key, type_account):
    flex = Flex(_id, key, type_account)
    await flex.cancel_order()


def get_tx_count(type_account):
    asyncio.run(check_tx(type_account))
