# EvolMoE (PYC-Encapsulated Version)

## ⚠️ Attention

To prevent code plagiarism before official publication, we have encapsulated our source code using `.pyc` files. Only the public training interface is exposed for use.  
This setup allows us to manage and maintain the code securely during the review process.

When executed, the training interface will automatically:

- Generate `actor_plot.png` and `critic_plot.png` to visualize learning trends.
- Save model parameters every 10,000 steps into the `saved_models/` directory.

## 🚀 How to Run

```bash
python train_network.py

