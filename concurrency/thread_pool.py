from concurrent.futures import ThreadPoolExecutor, as_completed

def threads(func,maxwork,ip_range_list):
    """thread"""

    resulte = []

    with ThreadPoolExecutor(max_workers=maxwork) as executor:

        futures = {executor.submit(func, i): i for i in ip_range_list}


        for future in as_completed(futures):
            result = future.result()
            if result:
                resulte.append(result)
    return resulte


