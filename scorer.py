def judge(question: str, expects: str, answer:str, results) -> dict:
    expects = expects.strip().lower()
    answer = (answer or "").lower()
    return {
        1: bool(expects) and any(expects in r.text.lower() for r in results),
        2: any(r.source.lower() in answer for r in results),
        4: all(len(r.text) <= 400 for r in results),
    }
