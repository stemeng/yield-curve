for scadenza in range(1,31):

    for tentativo in range(3):

        try:

            df = ecbdata.get_series(
                f"{serie}{scadenza}Y",
                start=inizio
            )

            break

        except Exception as e:

            print(
                f"{scadenza}Y tentativo {tentativo+1}/3 fallito"
            )

            if tentativo < 2:
                time.sleep(10)
            else:
                raise

    df["TIME_PERIOD"] = pd.to_datetime(df["TIME_PERIOD"])
    ...
