# Production Checklist

Before pushing this repository to production (making it your public GitHub profile), please verify the following:

- [x] **SVGs Cleaned:** Both `dark_mode.svg` and `light_mode.svg` contain the updated text and proper colors.
- [x] **ASCII Portrait:** Dark mode retains the ASCII portrait; Light mode is clean and empty on the left.
- [x] **No Unused Code:** All temporary scripts, generated artifacts, cache files, and debugging `.txt` files have been permanently removed.
- [x] **GitHub Actions Workflow:** The `.github/workflows/build.yaml` file is correctly configured to run `today.py` every 12 hours.
- [x] **Requirements & Environment:** `requirements.txt`, `.gitignore`, and `.env.example` are properly set up.
- [ ] **Secrets Configured:** You have added `ACCESS_TOKEN` and `USER_NAME` to your GitHub Repository Secrets.
- [ ] **Dynamic Update Test:** Run `python today.py` locally once with your secrets to ensure the SVG statistics update without breaking the layout.
