# main.py
import argparse
from chat import chat

VERSION = "0.2.0"

def main():
    parser = argparse.ArgumentParser(
        prog="deepseek",
        description="🤖 Chat with DeepSeek CLI (default: deepseek-chat)"
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
        help="显示版本号"
    )

    parser.add_argument(
        "--reasoner",
        action="store_true",
        help="使用 deepseek-reasoner 模型（默认使用 deepseek-chat）"
    )

    args = parser.parse_args()

    model = "deepseek-reasoner" if args.reasoner else "deepseek-chat"
    chat(model=model)
