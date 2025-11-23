#!/usr/bin/env python3
"""
GitHub Classroom Autograding Helper
為單一題目執行測試並返回分數
"""
import sys
import os
import subprocess
import yaml

def test_problem(problem_id):
    """測試單一題目並返回分數"""
    # 讀取配置
    with open('config/config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    if problem_id not in config['problems']:
        print(f"Error: Problem {problem_id} not found in config", file=sys.stderr)
        return 1
    
    problem = config['problems'][problem_id]
    max_points = problem.get('points', 100)
    
    # 執行測試
    result = subprocess.run(
        ['python3', 'run_tests.py', problem_id],
        capture_output=True,
        text=True
    )
    
    # 讀取分數檔案
    score_file = f'build/{problem_id}.score'
    if os.path.exists(score_file):
        with open(score_file, 'r') as f:
            score, max_score = map(int, f.read().strip().split())
        
        print(f"{score}/{max_score}")
        
        # 返回 0 如果滿分，否則返回 1
        return 0 if score == max_score else 1
    else:
        print(f"0/{max_points}")
        return 1

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 test_single_problem.py <problem_id>", file=sys.stderr)
        sys.exit(1)
    
    problem_id = sys.argv[1]
    sys.exit(test_problem(problem_id))
