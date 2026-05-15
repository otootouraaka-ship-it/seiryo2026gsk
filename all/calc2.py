def make_data(df, ANSWER_KEY):

    # =====================================
    # 採点
    # =====================================

    scores = []

    for _, row in df.iterrows():

        score = 0

        for q, setting in ANSWER_KEY.items():

            correct = setting["answer"]

            point = setting["point"]

            if str(row[q]).strip() == correct:

                score += point

        scores.append(score)

    df["score"] = scores

    # =====================================
    # 統計
    # =====================================

    mean_score = df["score"].mean()

    std_score = df["score"].std()

    max_score = sum(
        x["point"]
        for x in ANSWER_KEY.values()
    )

    accuracy = (
        df["score"].sum()
        / (len(df) * max_score)
    ) * 100

    if std_score != 0:

        df["hensachi"] = (
            50
            + 10 *
            (df["score"] - mean_score)
            / std_score
        )

    else:

        df["hensachi"] = 50

    df["rank"] = (
        df["score"]
        .rank(
            ascending=False,
            method="min"
        )
        .astype(int)
    )

    return df, mean_score, std_score, max_score, accuracy