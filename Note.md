## Conferences
You may find inspiration for topics from the following conferences:
_ Computer Graphics: SIGGRAPH, SIGGRAPH Asia
_ Computer Vision: CVPR, ICCV, ECCV, WACV
_ AI / Machine Learning: ICML, ICLR, NeurIPS, AAAI
_ Multimedia: ACM Multimedia
_ Natural Language Processing: ACL, COLING, EMNLP
_ Speech: ICASSP, Interspeech
You can search for papers and ideas from these websites:
_ https://openaccess.thecvf.com
_ https://kesen.realtimerendering.com
_ https://openreview.net
_ https://arxiv.org
_ https://scholar.google.com 

## Tên đề tài
Adaptive Test-Time Compute Allocation via Optimal Stopping for Mathematical Reasoning
## Bài toán
LLM Reasoning $\rightarrow$ tự động điều chỉnh số lượng chuỗi suy luận (sampling budget) linh hoạt cho từng câu hỏi, bài dễ dừng sớm, bài khó dồn tài nguyên suy nghĩ nhiều hơn thay vì lấy mẫu cố định (Best-of-N)
## Vấn đề
Các kỹ thuật scaling test-time compute hiện nay (Self-Consistency, Best-of-N) dùng ngân sách cố định cho mọi bài, gây lãng phí token vào các bài dễ; đồng thời việc thiếu cơ chế hiệu chuẩn độ tin cậy (uncertainty calibration) khiến mô hình dừng sai ở các nhánh lỗi có độ tự tin ảo (overconfident error paths)
## Baseline
Self-Consistency CoT (FranxYao/chain-of-thought-hub)
Verifier-guided Best-of-N (openai/prm800k)
## Kì vọng 2.5 tháng
tái lập baseline Best-of-16/Majority Voting trên GSM8k & MATH, hoàn thiện thuật toán dừng tối ưu giúp giữ nguyên độ chính xác (Pass@1) nhưng tiết kiệm số token sinh ra