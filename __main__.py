import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="secure-agent-sandbox")
    parser.add_argument("--version", action="store_true", help="Print version and exit")
    args = parser.parse_args()

    if args.version:
        from secure_agent_sandbox import __version__
        print(__version__)
        return

    print("Secure Agent Sandbox: bootstrap ok. (Environment and bench runner to be added.)")


if __name__ == "__main__":
    main()
