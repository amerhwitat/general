from dataclasses import dataclass

@dataclass(frozen=True)
class HostingTarget:
    name: str
    kind: str
    deploy_command: str
    notes: str

FREE_HOSTS = (
    HostingTarget('GitHub Pages', 'static', 'git push origin main', 'Static sites/docs; enable Pages in repository settings.'),
    HostingTarget('Cloudflare Pages', 'static-edge', 'npx wrangler pages deploy <dir>', 'Requires a Cloudflare account and authenticated Wrangler; Git integration can auto-deploy.'),
    HostingTarget('Vercel', 'frontend', 'npx vercel --prod', 'Requires an authenticated Vercel CLI/account.'),
    HostingTarget('Netlify', 'static-functions', 'npx netlify deploy --prod', 'Requires an authenticated Netlify CLI/account.'),
    HostingTarget('Render', 'service', 'render deploy', 'Use the provider workflow/API after configuring an authenticated account.'),
)

def targets() -> list[dict]:
    return [t.__dict__ for t in FREE_HOSTS]


def generate_deploy_readme(project_name: str) -> str:
    lines = [f'# Deployment: {project_name}', '', 'Deploy only after reviewing generated code and provider permissions.', '']
    for target in FREE_HOSTS:
        lines += [f'## {target.name}', f'`{target.deploy_command}`', target.notes, '']
    return '\n'.join(lines)
