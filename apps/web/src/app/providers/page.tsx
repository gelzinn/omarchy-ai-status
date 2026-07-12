import { Header } from "@/components/header";
import { Footer } from "@/components/footer";
import { SUPPORTED_PROVIDERS } from "@ai-status/shared";
import { site, LIB_NAME } from "@/lib/env";
import { ShieldCheck } from "lucide-react";
import { ProviderSearch } from "@/components/provider-search";
import type { Metadata } from "next";

export const metadata: Metadata = {
	title: `Supported Providers | ${site.name}`,
	description: `Every AI provider ${LIB_NAME} can track in your Waybar — what each one reports and where it reads your credentials from.`,
};

export default function ProvidersPage() {
	return (
		<div className="mx-auto flex max-w-7xl flex-col gap-8 sm:gap-16 p-6 sm:py-16">
			<Header />

			<main className="flex flex-col gap-8 sm:gap-16 mt-8 lg:mt-0">
				{/* Hero — plain text, like the home hero */}
				<section className="flex flex-col gap-8">
					<h1 className="font-heading max-w-2xl text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
						Supported Providers
					</h1>
					<p className="max-w-2xl text-lg text-muted-foreground">
						Every AI service {LIB_NAME} can track in your Waybar — what each one
						reports, and where it reads your credentials from.
					</p>
				</section>

				{/* Search + provider grid */}
				<ProviderSearch providers={SUPPORTED_PROVIDERS} />

				{/* Security note */}
				<section className="flex items-start gap-3 rounded-2xl border border-border bg-card/40 p-4 text-sm">
					<ShieldCheck className="mt-0.5 size-5 shrink-0 text-foreground/70" />

					<div className="flex flex-col gap-2 leading-relaxed">
						<span className="font-medium text-foreground">
							Your credentials never leave your machine.
						</span>

						<div className="text-muted-foreground">
							<p>
								{site.name} ships zero API keys. Every provider reads its tokens
								directly from the auth files you already keep on disk — OAuth
								sessions, config files, cookies. Your machine talks straight to
								each provider's API. Nothing passes through us. No telemetry, no
								cloud proxy, no remote storage. Credentials live and die on your
								machine.
							</p>
						</div>
					</div>
				</section>
			</main>

			<Footer />
		</div>
	);
}
