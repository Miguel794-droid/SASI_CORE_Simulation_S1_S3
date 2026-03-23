import argparse
from .runner import run_benchmark
from .reporter import print_leaderboard, generate_report
from human_veto.models import mock_generate, GroqModel

def main():
    parser = argparse.ArgumentParser(description="Constitutional Red Teaming Benchmark")
    parser.add_argument("--model", default="mock", help="Model name or 'mock'")
    parser.add_argument("--groq-key", help="Groq API key for real models")
    args = parser.parse_args()
    
    if args.groq_key:
        groq = GroqModel(args.groq_key, model=args.model)
        model_fn = groq.generate
    else:
        model_fn = mock_generate
    
    results = run_benchmark(model_fn)
    print_leaderboard(results)
    generate_report(results)

if __name__ == "__main__":
    main()
